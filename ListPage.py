from tools import *
from Author import *
from Institutions import *

class Box:
    def __init__(self, box, box_type="author"):
        self.box = box # a webdriver element of class "mv2"
        self.box_type = box_type
        self.title = None
        self.id = None
        self.top = None
        self.middle = None
        self.bottom = None
        self.info = {}
        self.compile()

    def _compile_institution(self):
        self.info = {}
        rows = self.box.find_elements_by_class_name("ant-row")
        # find title and id
        self.title = rows[0].text
        id = self.box.find_element_by_tag_name("a").get_attribute("href")
        self.id = int(id.replace(URL_INSTITUTIONS,""))
        # address and country id
        address = ""
        self.top = rows[1]
        self.middle = rows[2]
        try:
            address += self.top.text + " "
        except:
            address += ""
        try:
            address += self.middle.text
        except:
            address += ""
        country_id = get_country_id(address)
        # n_papers, website
        self.bottom = rows[3].find_elements_by_class_name("ant-col")
        try:
            Website = self.bottom[0].find_element_by_tag_name("a").get_attribute("href")
        except:
            Website = None
        try:
            Papers = convert_str_to_int(self.bottom[1].text.replace("papers","").strip())
        except:
            Papers = None
        self.info = {"Id":self.id, "Name":self.title, "Website":Website,
                     "Papers":Papers, "Address":address,
                     "Country_id":country_id}

    def _compile_author(self):
        self.info = {}
        # find title and id
        title = self.box.find_element_by_class_name("result-item-title")
        self.title = title.text.split("(")[0]
        id = self.box.find_element_by_tag_name("a").get_attribute("href")
        self.id = int(id.replace(URL_AUTHORS,""))
        # find research_areas and experiments
        try:
            temp = self.box.find_element_by_class_name("mt1")
            temp = temp.find_elements_by_class_name("__InlineList__")
        except:
            temp = []
        if len(temp) == 2:
            self.top = get_research_areas(temp[0].text)
            self.middle = temp[1].text.replace("Experiments:","").strip()
        elif len(temp) == 1:
            self.top = get_research_areas(temp[0].text)
        self.bottom = None
        self.info = {"Id":self.id, "Name":self.title,
                "Research_areas":self.top, "Experiments":self.middle}

    def compile(self):
        if self.box_type == "institutions":
            self._compile_institution()
        if self.box_type == "authors":
            self._compile_author()

    def __str__(self):
        s = ""
        for key, value in self.info.items():
            s += str(key) + ": "
            s += str(value) + "\n"
        return s

class ListPage():
    def __init__(self, page_type="institutions",
                 max_items = NEXT_MAX_ITEMS_IN_PAGE,
                 query_type = "",
                 page_number = 1,
                 institution_id = None,
                 id = None,
                 q=""):

        self.url_motor = InspirehepURL()
        self.page_type = page_type
        self.url = self.url_motor.get_url(page_type=page_type, max_items=max_items,
                         page_number=page_number, query_type=query_type,
                         institution_id=institution_id, q=q)
        self.n_results = 0
        self.n_pages = 0
        self.n_remained = 0
        self.boxes = []
        self.max_items = max_items
        self.all_ids = "" # ids which are previously in database

    def _find_all_ids(self):
        # find ids which are already in database and ignore them
        table_name = self.page_type[0].upper() + self.page_type[1:]
        stmt = "SELECT Id FROM {}".format(table_name)
        all_ids = DB.connection.execute(stmt).fetchall()
        self.all_ids = [elem[0] for elem in all_ids]

    def _find_n_results(self):
        n_results = BROWSER.find_element_by_tag_name("main").text.split("\n")[0].split()[0].strip()
        self.n_results = convert_str_to_int(n_results)

    def _find_n_pages(self):
        self.n_pages = self.n_results // self.max_items

    def _find_n_remained(self):
        self.n_remained = self.n_results - self.n_pages*self.max_items

    def _find_boxes(self):
        self.boxes = BROWSER.find_elements_by_class_name("mv2")
        self.boxes = [Box(box, box_type=self.page_type) for box in self.boxes]

    def _insert_box_to_db_authors(self, box, db=DB):
        if box.info["Id"] in self.all_ids:
            print("id = {} is already in database ...".format(box.info["Id"]))
            return
        id = box.info["Id"]
        name = box.info["Name"]
        research_areas = box.info["Research_areas"]
        experiments = box.info["Experiments"]
        author = Author(id=id, name=name, research_areas=research_areas,
                        experiments=experiments)
        try:
            author.insert_to_database(db)
        except:
            print(author)

    def _insert_box_to_db_institutions(self, box, db=DB):
        if box.info["Id"] in self.all_ids:
            print("id = {} is already in database ...".format(box.info["Id"]))
            return
        id = box.info["Id"]
        name = box.info["Name"]
        address = box.info["Address"]
        website = box.info["Website"]
        country_id = box.info["Country_id"]
        papers_citeable = box.info["Papers"]
        institution = Institution(id=id, name=name, address=address,
                                  country_id=country_id, website=website,
                                  papers_citeable=papers_citeable)
        try:
            institution.insert_to_database(db)
        except:
            print(institution)

    def insert_box_to_db(self, box, db=DB):
        if self.page_type == "institutions":
            self._insert_box_to_db_institutions(box, db)
        if self.page_type == "authors":
            self._insert_box_to_db_authors(box, db)

    def compile(self):
        BROWSER.get(self.url)
        time.sleep(10)
        self._find_n_results()
        self._find_n_pages()
        self._find_n_remained()
        self._find_all_ids()
        print(self.__str__())

    def next(self):
        self.url = self.url_motor.next()
        BROWSER.get(self.url)
        time.sleep(10)

    def loop(self):

        self.compile()

        for n in range(self.n_pages + 1):
            # determine number of items in current page
            number = self.max_items
            if n == self.n_pages:
                number = self.n_remained
            self._find_boxes()
            for box in self.boxes[:number]:
                self.insert_box_to_db(box)
            self.next()


    def __str__(self):
        s = ""
        s += "number of results: {}\n".format(self.n_results)
        s += "number of pages: {}\n".format(self.n_pages)
        s += "number of remained: {}".format(self.n_remained)
        return s


def main():
    list_page = ListPage(page_type="authors", q="Javad Ebadi")
    #list_page = ListPage(page_type="institutions", q="China")
    list_page.loop()

if __name__ == "__main__":
    main()

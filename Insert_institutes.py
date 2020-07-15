# this script scrapes https://inspirehep.net/institutions
# and extracts primay information about all institutes
# such as id, name, address, country_id, website
# import internal packages
from tools import *

n_institutions_css_selector = "#root > section > main > div.w-100 > div > div > div:nth-child(1) > div > span"
url = "https://inspirehep.net/institutions?sort=mostrecent&size="+str(NEXT_MAX_ITEMS_IN_PAGE)+"&page=1"
BROWSER.get(url)
BROWSER.implicitly_wait(10)

# find number of pages of institutions in the website
n_institutions = convert_str_to_int(BROWSER.find_element_by_css_selector(n_institutions_css_selector).text.split()[0])
n_pages = n_institutions // NEXT_MAX_ITEMS_IN_PAGE
n_remained = n_institutions - NEXT_MAX_ITEMS_IN_PAGE*n_pages


# find ids which are already in database and ignore them
db = DatabaseAccessor()
all_ids = db.connection.execute("SELECT Id FROM Institutions").fetchall()
all_ids = [elem[0] for elem in all_ids]


def get_ith_institution_info(boxes, hrefs, upper_subboxes, i):
    name = upper_subboxes[i].text.split("\n")[0].replace("`"," ").replace("'","")
    address = upper_subboxes[i].text.replace("\n"," ").replace(name,"").strip().replace("`"," ").replace("'","")
    id = int(hrefs[i][0].get_attribute("href").replace(URL_INSTITUTIONS,""))
    website = hrefs[i][1].get_attribute("href")
    country_id = get_country_id(address)
    try:
        papers_citeable = convert_str_to_int(hrefs[i][2].text.replace("papers","").strip())
    except:
        papers_citeable = 0
    if URL_WEBPAGE in website:
        website=""
    return id, name, address, website, country_id, papers_citeable

def scrape(q=""):
    for j in range(n_pages+1):

        url = URL.get_url(page_type="institutions",
                          page_number=j+1,
                          q=q)
        BROWSER.get(url)
        BROWSER.implicitly_wait(15)
        boxes = BROWSER.find_elements_by_class_name("mv2")
        hrefs = [box.find_elements_by_tag_name("a") for box in boxes]
        upper_subboxes = [box.find_element_by_class_name("pa2") for box in boxes]

        number = NEXT_MAX_ITEMS_IN_PAGE
        if j == n_pages:
            number = n_remained
        for i in range(NEXT_MAX_ITEMS_IN_PAGE):
            id, name, address, website, country_id, papers_citeable = get_ith_institution_info(boxes, hrefs, upper_subboxes, i)
            if id in all_ids:
                print("id = {} is already in database ...".format(id))
                continue
            institution = Institution(id=id, name=name, address=address,
                                      country_id=country_id, website=website,
                                      papers_citeable=papers_citeable)
            try:
                institution.insert_to_database()
            except:
                print(institution)

words_list = ["Soviet", "North", "South", "Middle", "East", "West"]
words_list = words_list + ["Center", "Reseach", "Unlisted", "Institute", "Compangy", "Department", "University"]
words_list = [""] + words_list + COUNTRIES_LIST
for q in words_list:
    try:
        scrape(q)
    except IndexError:
        pass

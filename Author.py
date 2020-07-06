# import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from global_vars import *
from helper_functions import *
from database import *

# ***: remember to add other browsers or facilites to download


class AuthorCSSSelectors:
    def __init__(self):
        self.author_css = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > "
        self.full_name = self.author_css + "h2 > span"
        self.research_areas = self.author_css + "div.ant-row.ant-row-space-between > div.ant-col.mb3.ant-col-xs-24.ant-col-lg-12 > div.__InlineList__ > ul"
        self.affiliations_expand_button = self.author_css + "div.ant-row.ant-row-space-between > div:nth-child(2) > button"
        self.affiliations_css = self.author_css + "div.ant-row.ant-row-space-between > div:nth-child(2) > ul > li > div.ant-timeline-item-content > "
        self.affiliations_id = self.affiliations_css + "div:nth-child(2) > a"
        self.affiliations_years = self.affiliations_css + "div:nth-child(1)"
        self.affiliations_pos = self.affiliations_css + "div:nth-child(2)"

        # class name selectors
        self.show_citation_summary_button = "ant-switch"
        self.citation_table_class = "__CitationTable__"
        self.papers_list_class = "mv2"

        # css selectors
        self.next_page_disabled_attribute = "aria-disabled"
        self.next_page_existence = "li[title='Next Page']"
        self.next_page = "li[class='ant-pagination-next'] > a"


author_selector = AuthorCSSSelectors()


class Author:
    """
    class for authors
    """
    def __init__(self, id=0, full_name=""):
        self.id = id
        self.full_name = full_name
        self.url = URL_AUTHORS + str(id)
        self.research_areas = []
        self.affiliations_id = []
        self.affiliations_years = []
        self.affiliations_pos = []
        self.papers_citeable = 0
        self.papers_published = 0
        self.citations_citeable = 0
        self.citations_published = 0
        self.citation_per_paper_citeable = 0
        self.citation_per_paper_published = 0
        self.h_index_citeable = 0
        self.h_index_published = 0
        self.papers_id_list = []

    def get_PhD_id(self):
        assert( len(self.affiliations_id) == len(self.affiliations_pos) )
        for i in range(len(self.affiliations_pos)):
            if self.affiliations_pos[i].upper() == "PHD":
                return self.affiliations_id[i]
        return -1

    def insert_to_database(self):
        db = DatabaseAccessor()
        try:
            db.insert_Author(Id=self.id,
                             Name=self.full_name,
                             PhD_id=self.get_PhD_id()
                             )
        except:
            print("Author with id = {} is already in database, update instead of insert".format(self.id))
        db.close()

    def __str__(self):
        s = "Authr info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "full name:" + str(self.full_name) + "\n"
        s += "research areas: " + str(self.research_areas) + "\n"
        s += "affiliations id :" + str(self.affiliations_id) + "\n"
        s += "affiliations years:" + str(self.affiliations_years) + "\n"
        s += "affiliations position:" + str(self.affiliations_pos) + "\n"
        s += "    ========== Citation Table ==========" + "\n"
        s += "                 Citeable        Published" + "\n"
        s += "Papers              {}              {}     ".format(self.papers_citeable, self.papers_published) + "\n"
        s += "Citation            {}              {}     ".format(self.citations_citeable, self.citations_published) + "\n"
        s += "h index             {}              {}     ".format(self.h_index_citeable, self.h_index_published) + "\n"
        s += "Citation per Paper  {}              {}     ".format(self.citation_per_paper_citeable, self.citation_per_paper_published) + "\n"
        s += " ||||||>>>>> List of author's papers id: " + "\n"
        s += str(self.papers_id_list) + "\n"
        s += " ============================================== "
        return s


class AuthorScraper():
    def __init__(self, author, path_to_driver="chromedriver.exe"):
        self.navigation_page = 1
        self.affiliations_expand_status = False
        self.show_citation_summary_status = False
        self.browser = webdriver.Chrome(path_to_driver)
        self.browser.get(author.url)
        self.browser.implicitly_wait(20)  # time to wait for webpage to Load

    def _expand_affiliations(self):
        if self.affiliations_expand_status is False:
            try:
                next = self.browser.find_element_by_css_selector(author_selector.affiliations_expand_button)
                next.click()
            except:
                pass
            self.affiliations_expand_status = True
        else:
            return

    def _show_citation_summary(self):
        if self.show_citation_summary_status is False:
            try:
                next = self.browser.find_element_by_class_name(author_selector.show_citation_summary_button)
                next.click()
            except:
                pass
            self.show_citation_summary_status = True
        else:
            return

    def author_exists(self):
        if '404' in self.browser.current_url:
            print("HTTP Error 404: author with id={} does not exist".format(author.id))
            print("\n" + "Closing the driver ..." + "\n")
            self.close()
            return False
        else:
            return True

    def get_full_name(self):
        full_name = self.browser.find_element_by_css_selector(author_selector.full_name).text.split("(")[0].strip()
        return full_name

    def get_research_areas(self):
        try:
            TEMP = self.browser.find_element_by_css_selector(author_selector.research_areas)
            research_areas = [research_area.text for research_area in TEMP.find_elements_by_tag_name("li")]
        except:
            research_areas = []
        return research_areas

    def get_affiliations_id(self):
        self._expand_affiliations()
        affiliations_id = self.browser.find_elements_by_css_selector(author_selector.affiliations_id)
        affiliations_id = [int(t.get_attribute("href")[len(URL_INSTITUTIONS):]) for t in affiliations_id]
        affiliations_id = list(reversed(affiliations_id))
        return affiliations_id

    def get_affiliations_years(self):
        self._expand_affiliations()
        affiliations_years = self.browser.find_elements_by_css_selector(author_selector.affiliations_years)
        affiliations_years = list(reversed([year.text.split("-") for year in affiliations_years]))
        print(affiliations_years)
        affiliations_years = merge_years_for_lists_of_list(affiliations_years)
        return affiliations_years

    def get_affiliations_pos(self):
        self._expand_affiliations()
        try:
            affiliations_pos = self.browser.find_elements_by_css_selector(author_selector.affiliations_pos)
            affiliations_pos = [separate_affiliations_from_pos(position.text) for position in affiliations_pos]
        except ValueError:
            print("No affiliations are avaible for the author ...")
            affiliations_pos = []
        affiliations_pos = list(reversed(affiliations_pos))
        print(affiliations_pos)
        print("==================")
        return affiliations_pos

    def get_citation_table(self):
        self._show_citation_summary()
        table = self.browser.find_element_by_class_name(author_selector.citation_table_class)
        table = table.text.split("\n")
        papers = table[1].split()
        citations = table[2].split()
        h_index = table[3].split()
        citation_per_paper = table[4].split()

        citation_table = dict()
        citation_table["papers_citeable"] = convert_str_to_int(papers[len(papers) - 2])
        citation_table["papers_published"] = convert_str_to_int(papers[len(papers) - 1])
        citation_table["citations_citeable"] = convert_str_to_int(citations[len(citations) - 2])
        citation_table["citations_published"] = convert_str_to_int(citations[len(citations) - 1])
        citation_table["h_index_citeable"] = convert_str_to_int(h_index[len(h_index) - 2])
        citation_table["h_index_published"] = convert_str_to_int(h_index[len(h_index) - 1])
        citation_table["citation_per_paper_citeable"] = citation_per_paper[len(citation_per_paper) - 2]
        citation_table["citation_per_paper_published"] = citation_per_paper[len(citation_per_paper) - 1]

        return citation_table

    def navigate_to_next_page(self):
        button = self.browser.find_element_by_css_selector(author_selector.next_page)
        button.click()
        self.browser.implicitly_wait(10)
        time.sleep(10)
        self.navigation_page += 1
        # ActionChains(self.browser).move_to_element(button).click(button).perform()

    def get_papers_id_list_in_page(self, number=MAX_ITEMS_IN_PAGE):
        """gets papers id in author profile which are in one page"""
        papers_list = self.browser.find_elements_by_class_name(author_selector.papers_list_class)[:number]
        papers_list = [p.find_element_by_tag_name("a").get_attribute("href") for p in papers_list]
        papers_list = ([int(p.replace(URL_LITERATURE, "")) for p in papers_list])
        return papers_list

    def get_papers_id_list(self, papers_citeable):
        papers_id_list = []
        max_papers_in_page = 25
        n_loop = papers_citeable // max_papers_in_page
        n_remaining = papers_citeable % max_papers_in_page

        for i in range(n_loop):
            papers_id_list_in_page = self.get_papers_id_list_in_page(max_papers_in_page)
            print("papers number {} to {}".format(max_papers_in_page*i, max_papers_in_page*(i + 1)))
            print(papers_id_list_in_page)
            papers_id_list.extend(papers_id_list_in_page)
            self.navigate_to_next_page()

        if n_remaining != 0:
            papers_id_list_in_page = self.get_papers_id_list_in_page(n_remaining)
            papers_id_list.extend(papers_id_list_in_page)
            print(papers_id_list_in_page)

        return papers_id_list

    def close(self):
        self.browser.close()


def scrape_author(author):
    """scrape authors profile and fill its information in
    author object from Author class"""
    scraper = AuthorScraper(author)
    if not scraper.author_exists():
        return

    author.full_name = scraper.get_full_name()
    author.research_areas = scraper.get_research_areas()
    author.affiliations_id = scraper.get_affiliations_id()
    author.affiliations_years = scraper.get_affiliations_years()
    author.affiliations_pos = scraper.get_affiliations_pos()
    citation_table = scraper.get_citation_table()
    author.papers_citeable = citation_table["papers_citeable"]
    author.papers_published = citation_table["papers_published"]
    author.citations_citeable = citation_table["citations_citeable"]
    author.citations_published = citation_table["citations_published"]
    author.h_index_citeable = citation_table["h_index_citeable"]
    author.h_index_published = citation_table["h_index_published"]
    author.citation_per_paper_citeable = citation_table["citation_per_paper_citeable"]
    author.citation_per_paper_published = citation_table["citation_per_paper_published"]
    author.papers_id_list = scraper.get_papers_id_list(author.papers_citeable)

    scraper.close()


def main():
    authors_id = [1679997, 1471223, 1023812, 989083, 1021261, 1258934]
    authors_id = [1679997, 1471223]
    authors_id = [1021261]
    request_number = 0
    for author_id in authors_id:
        request_number += 1
        print("Request Number = {}".format(request_number))
        author = Author(author_id)
        scrape_author(author)

        print(author)
        author.insert_to_database()


if __name__ == "__main__":
    main()

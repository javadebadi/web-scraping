# import packages
from selenium import webdriver
import time

# create chrome webdriver browser
# ***: remember to add other browsers or facilites to download

URL_WEBPAGE = "https://inspirehep.net/"
URL_AUTHORS = URL_WEBPAGE + "authors/"
URL_INSTITUTIONS = URL_WEBPAGE + "institutions/"


class AuthorCSSSelectors:
    def __init__(self):
        self.full_name = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > h2 > span"
        self.research_areas = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div.ant-col.mb3.ant-col-xs-24.ant-col-lg-12 > div.__InlineList__ > ul"
        self.affiliations_id = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div:nth-child(2) > ul > li > div.ant-timeline-item-content > div:nth-child(2) > a"

class Author:
    """
    class for authors
    """
    def __init__(self, id = 0, full_name = ""):
        self.id = id
        self.full_name = full_name
        self.url = URL_AUTHORS + str(id)
        self.research_areas = []
        self.affiliations_id = []

    def __str__(self):
        s = "Authr info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "full name:" + str(self.full_name) + "\n"
        s += "research areas: " + str(self.research_areas) + "\n"
        s += "affiliations_id :" + str(self.affiliations_id) + "\n"
        return s


class AuthorScraper():
    def __init__(self, author, path_to_driver = "chromedriver.exe"):
        self.browser = webdriver.Chrome(path_to_driver)
        self.browser.get(author.url)
        self.browser.implicitly_wait(20) # time to wait for webpage to Load

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
        affiliations_id = self.browser.find_elements_by_css_selector(author_selector.affiliations_id)
        affiliations_id = [int(t.get_attribute("href")[len(URL_INSTITUTIONS):]) for t in affiliations_id]
        affiliations_id = list(reversed(affiliations_id))
        return affiliations_id

    def close(self):
        self.browser.close()


authors_id = [1679997, 1471223, 1023812, 989083, 1000]
request_number = 0
for author_id in authors_id:
    request_number += 1
    print("Request Number = {}".format(request_number))

    author = Author(author_id)
    author_selector = AuthorCSSSelectors()
    scraper = AuthorScraper(author)
    if not scraper.author_exists():
        continue


    author.full_name = scraper.get_full_name()
    author.research_areas = scraper.get_research_areas()
    author.affiliations_id = scraper.get_affiliations_id()

    scraper.close()
    print(author)
    #time.sleep(10)  #  10 second delay time for request from website

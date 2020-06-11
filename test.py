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



authors_id = [1679997, 1471223, 1023812, 989083, 1000]
request_number = 0
for author_id in authors_id:
    request_number += 1
    print("Request Number = {}".format(request_number))

    author = Author(author_id)
    author_selector = AuthorCSSSelectors()

    browser = webdriver.Chrome("chromedriver.exe")
    browser.get(author.url)
    browser.implicitly_wait(10)  # time to wait for webpage to Load
    if '404' in browser.current_url:
        print("HTTP Error 404: author with id={} does not exist".format(author_id))
        print("\n" + "Moving to next author_id ..." + "\n")
        continue

    # author research area
    author.full_name = browser.find_element_by_css_selector(author_selector.full_name).text.split("(")[0].strip()
    try:
        TEMP = browser.find_element_by_css_selector(author_selector.research_areas)
        author.research_areas = [research_area.text for research_area in TEMP.find_elements_by_tag_name("li")]
    except:
        pass


    # affiliations
    affiliations_id = browser.find_elements_by_css_selector(author_selector.affiliations_id)
    affiliations_id = [int(t.get_attribute("href")[len(URL_INSTITUTIONS):]) for t in affiliations_id]
    print(affiliations_id)
    author.affiliations_id = list(reversed(affiliations_id))

    browser.close()
    print(author)
    #time.sleep(10)  #  10 second delay time for request from website

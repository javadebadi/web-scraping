# import packages
from selenium import webdriver

# create chrome webdriver browser
# ***: remember to add other browsers or facilites to download

URL_AUTHORS = "https://inspirehep.net/authors/"

class AuthorCSSSelectors:
    def __init__(self):
        self.full_name = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > h2 > span"
        self.research_areas = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div.ant-col.mb3.ant-col-xs-24.ant-col-lg-12 > div.__InlineList__ > ul"

class Author:
    """
    class for authors
    """
    def __init__(self, id = 0, full_name = ""):
        self.id = id
        self.full_name = full_name
        self.url = URL_AUTHORS + str(id)
        self.research_areas = []

    def __str__(self):
        s = "Authr info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "full name:" + str(self.full_name) + "\n"
        s += "research areas: " + str(self.research_areas)
        return s



author = Author(1679997)
author = Author(100000)
author_selector = AuthorCSSSelectors()
browser = webdriver.Chrome("chromedriver.exe")
browser.get(author.url)
if '404' in browser.current_url:
    print("404 Error: author with id={} does not exist".format())
    exit()


author.full_name = browser.find_element_by_css_selector(author_selector.full_name).text.split("(")[0].strip()
TEMP = browser.find_element_by_css_selector(author_selector.research_areas)
author.research_areas = [research_area.text for research_area in TEMP.find_elements_by_tag_name("li")]
print(author)

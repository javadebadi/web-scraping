# import packages
from selenium import webdriver

# create chrome webdriver browser
# ***: remember to add other browsers or facilites to download

URL_AUTHORS = "https://inspirehep.net/authors/"

class AuthorCSSSelectors:
    def __init__(self):
        self.full_name = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > h2 > span:nth-child(1)"

class Author:
    """
    class for authors
    """
    def __init__(self, id = 0, full_name = ""):
        self.id = id
        self.full_name = full_name
        self.url = URL_AUTHORS + str(id)

    def __str__(self):
        s = "Authr info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "full name:" + str(self.full_name)
        return s



author = Author(1679997)
author_selector = AuthorCSSSelectors()
browser = webdriver.Chrome("chromedriver.exe")
browser.get(author.url)
author.full_name = browser.find_element_by_css_selector(author_selector.full_name).text.split("(")[0].strip()

print(author)

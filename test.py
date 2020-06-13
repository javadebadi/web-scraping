# import packages
from selenium import webdriver
import time

from global_vars import *

# ***: remember to add other browsers or facilites to download


# helper functions
def _merge_years_for_two_list(l1, l2):
    """a private method to merge two list of list where the last element of first list is equal to
    first element of the second list

    Args:
        l1 (list): first list
        l2 (list): second list

    Returns:
        l (list): merged list of l1 and l2

    Example:
            >>> _merge_years_for_two_list(['2013', '2014', '2015'],['2015', '2016', '2019'])
            ['2013', '2014', '2015', '2016', '2019']
    """
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    if l1[-1] == l2[0]:
        l = l1 + l2[1:]
    else:
        l = l1 + [''] +  l2
    return l

def _merge_years_for_lists_of_list(list_of_lists):
    """merge list of lists when last element of each list matches with the
    fist element of the next list

    Args:
        list_of_lists (list): a list of lists which will be merged

    Returns:
        l (list): a merged list of elements in lists of the list

    Example:
        >>> _merge_years_for_lists_of_list([["2010", "2012"], ["2012", "2014"], ["2014", "2020"]])
        ["2010", "2012", "2014", "2020"]
    """
    if len(list_of_lists) < 2:
        return list_of_lists[0]
    l = []
    for i in range(len(list_of_lists)):
        l = _merge_years_for_two_list(l, list_of_lists[i])
    return l

def separate_affiliations_from_pos(text):
    """A function to find affiliation position from a special type of string

    Args:
        text (str): a text which has forms of POSTION,AFFILIATION or AFFILIATION

    Returns:
        pos (str)
    """
    pos = text.split(",")[0].upper()
    if pos in AFFILIATIONS_POSITIONS:
        return pos
    else:
        return ''

class AuthorCSSSelectors:
    def __init__(self):
        self.full_name = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > h2 > span"
        self.research_areas = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div.ant-col.mb3.ant-col-xs-24.ant-col-lg-12 > div.__InlineList__ > ul"
        self.affiliations_expand_button = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div:nth-child(2) > button"
        self.affiliations_id = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div:nth-child(2) > ul > li > div.ant-timeline-item-content > div:nth-child(2) > a"
        self.affiliations_years = "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div:nth-child(2) > ul > li > div.ant-timeline-item-content > div:nth-child(1)"
        self.affiliations_pos =   "#root > section > main > div.__Authors__ > div > div > div.ant-row.ant-row-space-between.mv3 > div > div > div > div > div.pa2 > div > div.ant-row.ant-row-space-between > div:nth-child(2) > ul > li > div.ant-timeline-item-content > div:nth-child(2)"

author_selector = AuthorCSSSelectors()
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
        self.affiliations_years = []
        self.affiliations_pos = []

    def __str__(self):
        s = "Authr info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "full name:" + str(self.full_name) + "\n"
        s += "research areas: " + str(self.research_areas) + "\n"
        s += "affiliations id :" + str(self.affiliations_id) + "\n"
        s += "affiliations years:" + str(self.affiliations_years) + "\n"
        s += "affiliations position:" + str(self.affiliations_pos) + "\n"
        return s


class AuthorScraper():
    def __init__(self, author, path_to_driver = "chromedriver.exe"):
        self.affiliations_expand_status = False
        self.show_citation_summary_status = False
        self.browser = webdriver.Chrome(path_to_driver)
        self.browser.get(author.url)
        self.browser.implicitly_wait(10) # time to wait for webpage to Load

    def _expand_affiliations(self):
        if self.affiliations_expand_status == False:
            try:
                next = self.browser.find_element_by_css_selector(author_selector.affiliations_expand_button)
                next.click()
            except:
                pass
            self.affiliations_expand_status = True
        else:
            return

    def _show_citation_summary(self):
        if self.show_citation_summary_status == False:
            try:
                next = self.browser.find_element_by_class_name("ant-switch")
                next.click()
            except:
                pass
            self.show_citation_summary_status == True
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
        affiliations_years = _merge_years_for_lists_of_list(affiliations_years)
        return affiliations_years

    def get_affiliations_pos(self):
        self._expand_affiliations()
        try:
            affiliations_pos = self.browser.find_elements_by_css_selector(author_selector.affiliations_pos)
            affiliations_pos = [separate_affiliations_from_pos(position.text) for position in affiliations_pos]
        except:
            affiliations_pos = []
        affiliations_pos = list(reversed(affiliations_pos))
        print(affiliations_pos)
        print("==================")
        return affiliations_pos

    def close(self):
        self.browser.close()


def main():
    authors_id = [1679997, 1471223, 1023812, 989083, 1021261, 1258934]
    #authors_id = [1021261, 1258934]
    request_number = 0
    for author_id in authors_id:
        request_number += 1
        print("Request Number = {}".format(request_number))

        author = Author(author_id)
        scraper = AuthorScraper(author)
        if not scraper.author_exists():
            continue


        author.full_name = scraper.get_full_name()
        author.research_areas = scraper.get_research_areas()
        author.affiliations_id = scraper.get_affiliations_id()
        author.affiliations_years = scraper.get_affiliations_years()
        author.affiliations_pos = scraper.get_affiliations_pos()

        scraper.close()
        print(author)
        #time.sleep(10)  #  10 second delay time for request from website

if __name__ == "__main__":
    main()

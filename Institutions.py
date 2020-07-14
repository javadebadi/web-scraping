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


class InstitutionCSSSelectors:
    def __init__(self):
        pass


institution_selector = InstitutionCSSSelectors()


class Institution:
    """
    class for Institutions
    """
    def __init__(self, id=0, scrape_depth="all", name="", address=None, website=None, country_id=None, papers_citeable=None):
        self.id = id
        self.scrape_depth = scrape_depth
        self.name = name
        self.address = address
        self.website = website
        self.country_id = country_id
        self.papers_citeable = papers_citeable
        self.url = URL_INSTITUTIONS + str(id)
        self.info = {}

    def _fill_info(self):
        self.info["Id"] = self.id
        self.info["Name"] = self.name
        self.info["Address"] = self.address
        self.info["Website"] = self.website
        self.info["Country_id"] = self.country_id
        self.info["Papers_citeable"] = self.papers_citeable

    def finalize(self):
        self._fill_info()

    def update_in_database(self, db):
        for key, value in self.info.items():
            if key == 'id': # ignore id information from update
                continue
            if value == None:
                pass
            else:
                db.update_Institution(self.id, key, value)

    def insert_to_database(self):
        self.finalize()
        db = DatabaseAccessor()
        try:
            db.insert_Institution(Id=self.id, Name=self.name,
                                 Address=self.address, Website=self.website,
                                 Country_id = self.country_id,
                                 Papers_citeable=self.papers_citeable)
            print("Added {} with id = {} to institutions table".format(self.name, self.id))
        except:
            print("Error in insertion of id = {}, ..., maybe already in database ...".format(self.id))

        db.close()

    def __str__(self):
        s = "Institutions info:\n"
        s += "id: " + str(self.id) + "\n"
        s += "name:" + str(self.name) + "\n"
        s += "address: " + str(self.address) + "\n"
        s += "website: " + str(self.website) + "\n"
        s += "country id: " + str(self.country_id) + "\n"
        s += "Number of citeable papers: "+ str(self.papers_citeable) + "\n"
        s += " ============================================== "
        return s


class InstitutionScraper():
    def __init__(self, institution, path_to_driver=PATH_TO_DRIVER):
        self.navigation_page = 1
        self.affiliations_expand_status = False
        self.show_citation_summary_status = False
        self.browser = webdriver.Chrome(path_to_driver)
        self.browser.get(Institution.url)
        self.browser.implicitly_wait(20)  # time to wait for webpage to Load

    def Institution_exists(self):
        if '404' in self.browser.current_url:
            print("HTTP Error 404: institution with id={} does not exist".format(institution.id))
            print("\n" + "Closing the driver ..." + "\n")
            self.close()
            return False
        else:
            return True

def main():
    pass

if __name__ == "__main__":
    main()

# to get URL of different webpages based on
# query or based on id
from global_vars import *
from helper_functions import *

class InspirehepURL:
    def __init__(self):
        self.page_number = None
        self.url = None

    def get_url_id(self, page_type="authors", id=None):
        if page_type == "literature":
            return URL_LITERATURE + str(id)
        if page_type == "authors":
            return URL_AUTHORS + str(id)
        if page_type == "institutions":
            return URL_INSTITUTIONS + str(id)
        if page_type == "jobs":
            return URL_JOBS + str(id)
        if page_type == "seminars":
            return URL_SEMINARS + str(id)
        if page_type == "conferences":
            return URL_CONFERENCES + str(id)
        else:
            raise ValueError("page_type {} is invalid ".format(page_type))

    def _get_url_part_of_query_type(self, query_type=""):
        if query_type == "":
            return ""
        if query_type == "ai":
            return "positions.record.%24ref%3A"

    def get_url(self, page_type="authors", max_items=NEXT_MAX_ITEMS_IN_PAGE,
                page_number=1, query_type="", institution_id=None, q=""):
        """Returns the url of a search in inspirehep website
        Args:
            page_type (str): page determines what kind of information
                is queried in the website
                it can have these values: "authors", "institutions"
                    "jobs", "literature", "seminars", "conferences"
            max_items (int): determines the maximum number of items
                or boxes in page
            page_number (int): determines the page number in a give query
            query_type (str): the query type determines what kind of query
                is wantet. it can have following values:
                    "" which is desired
                    "ai" stands for authors of instituion
            institiution_id (int): determines the id for institutions which might
                be used in query
            q (str): determines the query statement which is an arbitrary string


        Returns:
            url (str): the url of a webpage we want to scrape as a list of simliar
                items

        Raises:
            ValueError: when the page_type in not one of the determined values
            ValueError: when the query_type in "ai" the q must not be given
        """
        self.url = URL_WEBPAGE
        self.page_number = page_number
        if page_type not in ["authors", "institutions", "conferences", "seminars", "jobs", "literature"]:
            raise ValueError("page_type = {} is not allowed".format(page_type))
        self.url += page_type + "?sort=mostrecent&size=" + str(max_items) + "&page=" + str(page_number)
        if query_type == 'ai' and q != "":
            raise ValueError("""Could not query authors of institution and
                arbitrary query at the same time. Give only one of q or instiution_id
                arguments to the function""")
        if institution_id:
            self.url += "&q=" + self._get_url_part_of_query_type("ai") + str(institution_id)
        else:
            self.url += "&q=" + q
        return self.url

    def next(self):
        """returns the next page of url and sets the self.url to next url also"""
        if self.page_number == None:
            raise TypeError("""initial url does not have page_number ..., so
                            the next page is not defined""")

        current_page_query = "&page="+str(self.page_number)
        self.page_number += 1
        next_page_query = "&page="+str(self.page_number)
        self.url = self.url.replace(current_page_query, next_page_query)
        return self.url

def main():
    url = InspirehepURL()
    url.get_url(page_type="authors", query_type="ai", institution_id=906446)
    print(url.url)
    print(url.next())
    url.get_url(page_type="institutions", page_number=2, query_type="", q="USA")

if __name__ == "__main__":
    main()

PC = "JAVAD"
# PC = "MORTEZA"
OS = "WINDOWS"
# OS = "LINUX"
# OS = "MAC"
URL_WEBPAGE = "https://inspirehep.net/"
URL_AUTHORS = URL_WEBPAGE + "authors/"
URL_INSTITUTIONS = URL_WEBPAGE + "institutions/"
URL_LITERATURE = URL_WEBPAGE + "literature/"
URL_JOBS = URL_WEBPAGE + "jobs/"
URL_SEMINARS = URL_WEBPAGE + "seminars/"
URL_CONFERENCES = URL_WEBPAGE + "conferences/"

# affiliations
AFFILIATIONS_POSITIONS = [
        "SENIOR",
        "POSTDOC",
        "PHD",
        "UNDERGRADUATE",
        "MASTER",
        "MS", "BA",
        "MSC",
        "BSC",
        "MA",
        "VISITOR"
]

MAX_ITEMS_IN_PAGE = 25

DB_NAME = "hep.sqlite"

if OS == "WINDOWS":
    if PC == "JAVAD":
        WORKING_PATH = "C:\\Users\\Javad\\github\\web-scraping\\"
else:
    WORKING_PATH = ""

DB_PATH = "sqlite:///" + WORKING_PATH + DB_NAME

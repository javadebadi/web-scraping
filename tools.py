# import external packages
from selenium import webdriver
import time
# import internal packages
from global_vars import *
from helper_functions import *
from InspirehepURL import *
from Author import *
from Institutions import *
from database import *


URL = InspirehepURL()
BROWSER = webdriver.Chrome(PATH_TO_DRIVER)

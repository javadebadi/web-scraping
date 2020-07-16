# import external packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# import internal packages
from global_vars import *
from helper_functions import *
from InspirehepURL import *
from database import *

URL = InspirehepURL()
BROWSER = webdriver.Chrome(PATH_TO_DRIVER)
DB = DatabaseAccessor()

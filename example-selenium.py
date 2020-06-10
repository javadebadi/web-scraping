from selenium import webdriver
# add chromedriver path
browser = webdriver.Chrome("chromedriver.exe")
# get website
browser.get("https://www.reddit.com")
# find elements by class name or etc
gen_output = browser.find_elements_by_class_name("_2Jjv0TAohMSydVpAgyhjhA")
# get texts form elements
print([elem.text for elem in gen_output])

# get links from the website and go to other website
get_div = browser.find_element_by_class_name("_3GfG_jvS9X-90Q_8zU4uCu:first-child")
link = get_div.find_element_by_tag_name("a").get_attribute("href")
next_url = browser.get(link)

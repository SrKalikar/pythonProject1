from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from urllib.request import Request
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.sanfoundry.com/database-mcqs-relational-database-schema/")
binary = FirefoxBinary('./geckodriver.exe')
#browser = webdriver.Firefox()
print(driver.title)
print(driver.current_url)
html = driver.context('entry-content')
x = driver.find_element_by_class_name('entry-content')
y = driver.find_element_by_class_name('collapseomatic_content')
#y = BeautifulSoup(html, "html.parser")
print(x.text)
print(y.text)





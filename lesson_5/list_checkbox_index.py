from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/career')
   time.sleep(3)
   select = Select(browser.find_element_by_name('filters[type]'))
   select.select_by_index(1)
   time.sleep(3)
finally:
   browser.quit()

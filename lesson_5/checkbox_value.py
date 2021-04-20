# Чтобы использовать методы класса Select, надо его импортировать.
# Далее мы создаём объект этого класса (checkbox), после чего можно использовать различные методы.
# Выбор на основе значения value:

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/career')
   time.sleep(3)
   select = Select(browser.find_element_by_name('filters[type]'))
   select.select_by_value("Компании")
   time.sleep(5)
finally:
   browser.quit()

# Этот метод позволяет получить значение какого-либо атрибута элемента.

import time

from selenium import webdriver

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/register')
   time.sleep(3)
   print(
       browser.find_element_by_css_selector('[type="email"]').get_attribute(
           "required"
       )
   )
   time.sleep(3)
finally:
   browser.quit()

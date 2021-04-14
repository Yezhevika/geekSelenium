# find_element_by_id(id)
# Осуществляет поиск по id. Создадим скрипт для поиска по id:
# в этом случае мы будем искать на странице элемент с id registration-form-button, а затем кликнем на него

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru')
   time.sleep(3)
   browser.find_element_by_id('gb-analytics-sign-up').click()
   time.sleep(3)
finally:
   browser.quit()

# Написание скрипта для загрузки файла

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(1)
   email_field = browser.find_element_by_css_selector('[name="email"]')
   email_field.send_keys("samoylova.viktoriya.u@gmail.com")
   password_field = browser.find_element_by_css_selector('[name="password"]')
   password_field.send_keys("rjgbkrf")
   button_field = browser.find_element_by_css_selector('button.button').click()
   time.sleep(1)

# Переход во вкладку Загрузка файла
   many_fields = browser.find_element_by_css_selector('[href="/uploading"].navbar-item').click()

# Тап по кнопке Выбор файла и загрузка файла

   input_area = browser.find_element_by_css_selector('[type="file"]')
   input_area.send_keys(os.path.join(os.getcwd(), "resources", 'рамси.jpg'))

# Нажать кнопку Загрузить

   button_field = browser.find_element_by_css_selector('[type="submit"]').click()
   time.sleep(2)

# Обновить страницу и убедиться что сообщение об успехе пропало

   browser.refresh()
   time.sleep(2)

finally:
   browser.quit()

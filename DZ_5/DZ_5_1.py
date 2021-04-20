# Написание скрипта для заполнения информации о себе

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

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

   many_fields = browser.find_element_by_css_selector('[href="/about2"].navbar-item').click()

   input_field = browser.find_element_by_css_selector('[name="name"]').send_keys("Виктория")

   input_field = browser.find_element_by_css_selector('[name="surname"]').send_keys("Самойлова")

# Специалист
   checkbox = browser.find_element_by_css_selector('[value="manual"]')
   checkbox = browser.find_element_by_css_selector('[value="auto"]').click()

# Языки программирования
   list = browser.find_element_by_css_selector('[value="Python"]').click()

# Уровень квалификации
#    select = browser.find_element_by_css_selector('.select > select').click()
#    select.select_by_value("Junior").click()
   select = Select(browser.find_element_by_name('lvl'))
   select.select_by_visible_text("Junior")

   button_field = browser.find_element_by_css_selector('button.button').click()
   answer = browser.find_element_by_css_selector('.notification')
   time.sleep(3)

finally:
   browser.quit()

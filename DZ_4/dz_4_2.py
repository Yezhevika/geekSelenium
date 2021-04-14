
from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(3)
   email_field = browser.find_element_by_css_selector('[name="email"]').send_keys("samoylova.viktoriya.u@gmail.com")
   password_field = browser.find_element_by_css_selector('[name="password"]').send_keys("rjgbkrf")
   button_field = browser.find_element_by_css_selector('button.button').click()
   many_fields = browser.find_element_by_css_selector('[href="/about1"].navbar-item').click()

   input_field = browser.find_element_by_css_selector('[name="name"]').send_keys("Виктория")

   input_field = browser.find_element_by_css_selector('[name="surname"]').send_keys("Самойлова")

   input_field = browser.find_element_by_css_selector('[name="email"]').send_keys("samoylova.viktoriya.u@gmail.com")

   input_field = browser.find_element_by_css_selector('[name="city"]').send_keys("Санкт-Петербург")
   time.sleep(1)

   button_field = browser.find_element_by_css_selector('button.button').click()
   answer = browser.find_element_by_css_selector('.notification')
   time.sleep(3)
finally:
   browser.quit()

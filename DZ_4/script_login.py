from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(3)
   email_field = browser.find_element_by_css_selector('[name="email"]')
   email_field.send_keys("samoylova.viktoriya.u@gmail.com")
   password_field = browser.find_element_by_css_selector('[name="password"]')
   password_field.send_keys("rjgbkrf")
   button_field = browser.find_element_by_css_selector('button.button').click()
   time.sleep(3)
finally:
   browser.quit()

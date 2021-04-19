# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# from selenium import webdriver
#
# import time
#
# browser = webdriver.Chrome()
# try:
#    browser.get('https://geekbrains.ru/')
#    time.sleep(3)
#    email_field = browser.find_element(By.NAME, 'user[email]')
#    email_field.send_keys('email@email.ru')
#    time.sleep(1)
#    password_field = browser.find_element(By.NAME, 'user[password]')
#    password_field.send_keys('password123')
#    password_field.send_keys(Keys.ENTER)
#
# finally:
#    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/login')
   time.sleep(3)
   email_field = browser.find_element(By.NAME, 'user[email]')
   email_field.send_keys('email@email.ru')
   time.sleep(1)
   password_field = browser.find_element(By.NAME, 'user[password]')
   password_field.send_keys('password')
   password_field.send_keys(Keys.NUMPAD1, Keys.NUMPAD2, Keys.NUMPAD3, Keys.ENTER)

finally:
   browser.quit()


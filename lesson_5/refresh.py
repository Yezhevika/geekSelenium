# import time
#
# browser = webdriver.Chrome()
# try:
#    browser.get('https://geekbrains.ru/')
#    time.sleep(2)
#    browser.refresh()
#    time.sleep(2)
# finally:
#    browser.quit()

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/')
   time.sleep(2)
   browser.find_element_by_id("gb-analytics-sign-in").click()
   time.sleep(1)
   browser.back()
   time.sleep(1)
   browser.forward()
   time.sleep(2)
finally:
   browser.quit()

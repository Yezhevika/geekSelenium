
from selenium import webdriver
import time

# browser = webdriver.Chrome()
# try:
#    browser.get('https://geekbrains.ru/login')
#    time.sleep(3)
#    browser.find_element_by_name('user[email]').send_keys("firsttestdemo@yandex.ru")
#    browser.find_element_by_id('user_password').send_keys('justforgb123')
#    browser.find_element_by_css_selector('[data-testid="login-submit"]').click()
#    time.sleep(3)
#    browser.find_element_by_class_name('gb-top-menu__user-avatar').click()
#    time.sleep(1)
#    browser.find_element_by_css_selector(".pull-right .icon-cog-small").click()
#    time.sleep(1)
#    browser.find_element_by_css_selector('[type="User::Avatar"]').click()
#    time.sleep(1)
#    input_area = browser.find_element_by_css_selector('[type="file"]')
#    input_area.send_keys("/Users/vika/Desktop/photo_2020-10-12_14-17-12 — копия.jpg")
#    time.sleep(4)
#    browser.find_element_by_css_selector('.image-cropper__save-button-wrapper [ng-hide="$ctrl.pending"]').click()
#    time.sleep(2)
# finally:
#    browser.quit()

from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
try:
    browser.get('https://geekbrains.ru/login')
    time.sleep(3)
    browser.find_element_by_name('user[email]').send_keys("firsttestdemo@yandex.ru")
    browser.find_element_by_id('user_password').send_keys('justforgb123')
    browser.find_element_by_css_selector('[data-testid="login-submit"]').click()
    time.sleep(3)
    browser.find_element_by_class_name('gb-top-menu__user-avatar').click()
    time.sleep(1)
    browser.find_element_by_css_selector(".pull-right .icon-cog-small").click()
    time.sleep(1)
    browser.find_element_by_css_selector('[type="User::Avatar"]').click()
    time.sleep(1)
    input_area = browser.find_element_by_css_selector('[type="file"]')
    input_area.send_keys(os.path.join(os.getcwd(), "resources", 'рамси.jpg'))
    time.sleep(4)
    browser.find_element_by_css_selector('.image-cropper__save-button-wrapper [ng-hide="$ctrl.pending"]').click()
    time.sleep(2)
finally:
    browser.quit()




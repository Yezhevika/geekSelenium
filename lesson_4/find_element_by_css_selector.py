# Этот метод осуществляет поиск по CSS-селектору.
# В качестве аргумента в него передаётся CSS-селектор, например .site-footer__icons .site-footer__icon:nth-child(1).
# В этом случае мы найдём иконку Facebook в футере и кликнем на неё

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/login')
   time.sleep(3)
   browser.find_element_by_css_selector(".site-footer__icons .site-footer__icon:nth-child(1)").click()
   time.sleep(3)
finally:
   browser.quit()
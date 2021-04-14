# Метод осуществляет поиск по name.
# Чтобы использовать этот метод, нам нужно передать в него в качестве аргумента значение атрибута name.
# Для ввода каких-либо данных в поле в Selenium используется метод send_keys.
# Можем попробовать использовать его для ввода данных в поле, атрибут которого name="user[email]"

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/login')
   time.sleep(3)
   email_field = browser.find_element_by_name("user[email]")
   email_field.send_keys("firsttestdemo@yandex.ru")
   time.sleep(3)
finally:
   browser.quit()

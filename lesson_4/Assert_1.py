# В тестах удобно использовать инструкцию assert для проверки истинности утверждения. Это позволяет проверять
# наличие элементов, значение атрибутов, текст и пр.
# После assert указывается утверждение, которое проверяется на истинность. После запятой указывается текст,
# который будет выведен, если проверка не пройдена

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru')
   time.sleep(3)
   assert browser.find_element_by_id('gb-analytics-sign-up').text == "Регистрация", "Неверный текст кнопки"
finally:
   browser.quit()

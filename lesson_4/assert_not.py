# Также можно использовать утверждение assert not.
# Если утверждение будет ложным, скрипт отработает успешно, а если истинным — возникнет ошибка.

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru')
   time.sleep(3)
   assert not browser.find_element_by_id('gb-analytics-sign-up').text == "Войти", "Неверный текст кнопки"
finally:
   browser.quit()
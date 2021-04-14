# find_element_by_class_name(class_name)
# Осуществляет поиск по имени класса. Попробуем использовать его в нашем скрипте.
# Перед поиском добавим ожидание, чтобы убедиться, что страница точно прогрузилась,
# а затем найдём иконку с именем класса vkontakte и кликнем на неё.
# Для клика на элемент Selenium используем метод click.

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru')
   time.sleep(3)
   browser.find_element_by_class_name('vkontakte').click()
   time.sleep(3)
finally:
   browser.quit()

# find_element_by_tag_name(name)
# Этот метод осуществляет поиск элемента по имени тега. Скорее всего, вам придётся использовать его редко,
# так как обычно на странице теги совпадают у нескольких элементов, а нужно составлять однозначные локаторы,
# по которым найдётся ровно один элемент. Для примера работы этого метода можно написать скрипт, который
# выводит на печать текст заголовка h2. Используем свойство text, которое возвращает текст элемента.

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/login')
   time.sleep(3)
   print(browser.find_element_by_tag_name("h2").text)
   time.sleep(3)
finally:
   browser.quit()


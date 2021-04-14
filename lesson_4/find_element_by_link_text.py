# find_element_by_link_text(link_text) и find_element_by_partial_link_text(link_text)
# Эти методы позволяют осуществлять поиск по полному (link_text) и частичному (partial_link_text) совпадению текста ссылки
# Однако использовать их нежелательно, так как текст может измениться. Также они не подходят для мультиязычных сайтов:
# на каждом языке текст будет отличаться. Лучше искать по другим признакам и обращаться к этим методам только в случае,
# если нет альтернативных вариантов.
# Пример использования метода find_element_by_link_text вы видите ниже. В этом случае полный текст элемента — «Отзывы».

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get('https://geekbrains.ru/login')
    time.sleep(3)
    browser.find_element_by_link_text("Отзывы").click()
    time.sleep(3)
finally:
    browser.quit()

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get('https://geekbrains.ru/login')
    time.sleep(3)
    browser.find_element_by_partial_link_text("проекте").click()
    time.sleep(3)
finally:
    browser.quit()
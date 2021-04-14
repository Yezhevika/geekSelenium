# Напишем скрипт для страницы «Курсы». Нужно выполнить следующие шаги:
# Перейти на страницу курсов https://courses.geekbrains.ru/.
# Убедиться, что текст заголовка — «Курсы по всем направлениям».
# Ввести в поле поиска слово Python.
# Напечатать количество найденных курсов.
# Для поиска элементов воспользуемся методом find_element и классом By.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
   browser.get('https://courses.geekbrains.ru/')
   time.sleep(3)
   title = browser.find_element(By.CSS_SELECTOR, "#top-page .mobile-heading")
   assert title.text == "Курсы по всем направлениям", "Неверный текст заголовка"
   search_field = browser.find_element(By.NAME, "name")
   search_field.send_keys("Python")
   time.sleep(3)
   course_cards = browser.find_elements(By.CSS_SELECTOR, '[class="uni-card w-dyn-item"]')
   print(len(course_cards))
finally:
   browser.quit()

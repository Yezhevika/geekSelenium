# Напишите скрипт, который выполнит следующее:
# Перейти на страницу «Поля ввода» http://test-stage.geekbrains.ru:8080/many_fields
# Ввести какую-либо строку в поле с уникальным селектором (оно там одно).
# Нажать на кнопку.
# Убедиться, что отобразилось сообщение об успехе (используйте свойство .text).
# Ввести какую-либо строку в любое другое поле.
# Убедиться, что отобразилось сообщение об ошибке (используйте свойство .text).
# Для поиска элементов используйте методы группы find_element_by.

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(3)
   email_field = browser.find_element_by_css_selector('[name="email"]')
   email_field.send_keys("samoylova.viktoriya.u@gmail.com")
# Вводим пароль для почты
   password_field = browser.find_element_by_css_selector('[name="password"]')
   password_field.send_keys("rjgbkrf")
# Тапнуть на кнопку подтверждения
   button_field = browser.find_element_by_css_selector('button.button').click()
# Перейти во вкладку Поля ввода
   many_fields = browser.find_element_by_css_selector('[href="/many_fields"].navbar-item').click()

# Вводим в правильное поле и тест проходит удачно

   input_field = browser.find_element_by_css_selector('[name="test"]').send_keys("Получилось!")
   button_field = browser.find_element_by_css_selector('button.button').click()
   answer = browser.find_element_by_css_selector('.notification')

   assert answer.text == "Успех.", "Неправильное поле."
   time.sleep(1)

# Вводим в неправильное поле и тест проходит удачно - т е отображается ошибка

   input_field = browser.find_element_by_css_selector('[name="field1"]').send_keys("Ждем ошибку!")
   button_field = browser.find_element_by_css_selector('button.button').click()
   answer = browser.find_element_by_css_selector('.notification')

   assert answer.text == "Успех.", "Неправильное поле."

   time.sleep(2)

finally:
   browser.quit()

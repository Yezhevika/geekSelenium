# Чекбокс — это элемент графического пользовательского интерфейса,
# позволяющий пользователю управлять параметром с двумя состояниями: включено и отключено.
#
# Радиобаттон — элемент интерфейса, который позволяет пользователю выбрать одну опцию (пункт)
# из предопределённого набора (группы)
#
# Проверяем, зажжён ли чекбокс, и если нет — кликнуть по нему

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('https://geekbrains.ru/career')
   time.sleep(3)
   checkbox = browser.find_element_by_css_selector('[name="filters[paid]"]')
   if not checkbox.get_attribute('checked'):
       checkbox.click()
   time.sleep(2)
finally:
   browser.quit()

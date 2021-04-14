# find_element_by_xpath(xpath)
# Этот метод использует в качестве локатора XPath элемента.
# Лучше стараться использовать в качестве локаторов значения различных атрибутов или CSS-селекторы,
# но иногда может потребоваться и этот метод.
# Для примера попробуем найти элемент //a[@data-testid="vkontakte-button"] и кликнуть на него

from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get('https://geekbrains.ru/login')
    time.sleep(3)
    browser.find_element_by_xpath('//a[@data-testid="vkontakte-button"]').click()
    time.sleep(3)
finally:
    browser.quit()


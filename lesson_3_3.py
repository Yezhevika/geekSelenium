from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get('https://geekbrains.ru/events')
    time.sleep(5)
finally:
    browser.quit()

# quit используется для полного завершения сессии браузера
# close закрывает только текущее окно браузера
# Чтобы браузер точно завершился даже в случае возникновения ошибки в процессе выполнения скрипта,
# используем конструкцию try-finally

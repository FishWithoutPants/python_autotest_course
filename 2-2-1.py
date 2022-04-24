from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    #x_element =
    x = browser.find_element(By.CSS_SELECTOR, value='#num1').text
    #y_element = browser.find_element(By.CSS_SELECTOR, value='#num2')
    y = browser.find_element(By.CSS_SELECTOR, value='#num2').text
    select = Select(browser.find_element(By.TAG_NAME, value="select"))
    select.select_by_value(str(int(x)+int(y)))
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
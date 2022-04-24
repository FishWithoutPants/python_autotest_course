from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element(By.CSS_SELECTOR, value='#input_value').text
    y = calc(int(x))
    input1 = browser.find_element(By.CSS_SELECTOR, value="#answer")
    input1.send_keys(y)
    time.sleep(0.5)
    button = browser.find_element(By.CSS_SELECTOR, value="#robotCheckbox")
    _ = button.location_once_scrolled_into_view
    time.sleep(0.5)
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, value="#robotsRule")
    _ = button.location_once_scrolled_into_view
    time.sleep(0.5)
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    _ = button.location_once_scrolled_into_view
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

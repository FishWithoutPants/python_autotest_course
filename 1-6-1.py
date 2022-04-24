from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, value='#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, value="#answer")
    input1.send_keys(y)
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, value="[for='robotCheckbox']")
    button.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, value="[for='robotsRule']")
    button.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
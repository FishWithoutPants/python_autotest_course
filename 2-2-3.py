import os
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input1 = browser.find_element(By.CSS_SELECTOR, value="[name= 'firstname']")
    input1.send_keys("Олег")
    time.sleep(0.5)
    input2 = browser.find_element(By.CSS_SELECTOR, value="[name= 'lastname']")
    input2.send_keys("Олег")
    time.sleep(0.5)
    input3 = browser.find_element(By.CSS_SELECTOR, value="[name= 'email']")
    input3.send_keys("email@email.email")
    time.sleep(0.5)
    input4 = browser.find_element(By.CSS_SELECTOR, value="[name= 'file']")
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    _ = button.location_once_scrolled_into_view
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
import os
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def input_by_css(input_text, css):
    input1 = browser.find_element(By.CSS_SELECTOR, value=css)
    input1.send_keys(input_text)


def click_by_css(css):
    button = browser.find_element(By.CSS_SELECTOR, value=css)
    button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    click_by_css("[type = submit]")
    time.sleep(0.5)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(0.5)
    x = browser.find_element(By.CSS_SELECTOR, value='#input_value').text
    y = calc(int(x))
    input1 = browser.find_element(By.CSS_SELECTOR, value="#answer")
    input1.send_keys(y)
    time.sleep(0.5)
    click_by_css("[type = submit]")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

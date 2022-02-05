from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"


def calc_x(x):
    return math.log(10,abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc_x(int(x))
    print(y)

    answer = browser.find_element(By.CSS_SELECTOR, ".form-control")
    answer.send_keys(y)

    checkbox_1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox_1.click()
    browser.execute_script("window.scrollBy(0, 150);")
    radio = browser.find_element(By.ID, "robotsRule")

    radio.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()
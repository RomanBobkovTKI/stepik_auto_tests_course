from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element(By.CSS_SELECTOR, "div.first_class > input[required]")
    input_1.send_keys("Roman")
    input_2 = browser.find_element(By.CSS_SELECTOR, "div.second_class > input[required]")
    input_2.send_keys("Bobkov")
    time.sleep(5)
    input_3 = browser.find_element(By.CSS_SELECTOR, "div.third_class > input[required]")
    input_3.send_keys("Хуй@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    h1 = browser.find_element(By.TAG_NAME, "h1")
    find_text = h1.text

    assert "Congratulations! You have successfully registered!" == find_text

finally:
    time.sleep(5)
    browser.quit()
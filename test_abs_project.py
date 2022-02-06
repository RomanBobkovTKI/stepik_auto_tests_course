from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":

    try:
        test_abs1()
        print("All tests passed!")

    
    finally:
        time.sleep(1)

import pandas as pd
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Name_Generator():
    def __init__(self) -> None:
        pass

    def generate(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get('http://random-name-generator.info/')

        num_button = driver.find_element(By.XPATH, "//select[contains(@name, 'n')]")
        num_button.click()
        number = num_button.find_element(By.XPATH, ".//option[contains(@value, '100')]")
        number.click()
        gen_num = driver.find_element(By.XPATH, "//input[contains(@id, 'submit')]")
        gen_num.click()

        names = driver.find_elements(By.XPATH, "//ol[contains(@class, 'nameList')]/li")

        random_name = []

        for name in names:
            random_name.append(name.text)

        time.sleep(2)

        driver.quit()
        return random_name
    
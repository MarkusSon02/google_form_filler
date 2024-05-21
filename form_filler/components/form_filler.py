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

class Form_filler:
    def __init__(self, driver):
        self.driver = driver

    def get_form(self, form):
        self.driver.get(form)

    def close_form(self):
        self.driver.close()

    def fill_form(self, form, file):
        df = pd.read_excel(file)
        # Iterate over the rows of the DataFrame
        for index, row in df.iterrows():
            self.get_form(form)
            self.driver.implicitly_wait(random.randint(10, 15))
            time.sleep(2)
            elements = self.driver.find_elements(By.XPATH, '//input[contains(@class, "whsOnd zHQkBf")]')
            # Access each cell in the row
            i = 0
            for col in df.columns:
                if i < 3:
                    elements[i].send_keys(row[col])
                elif i == 3:
                    option_tickboxes = self.driver.find_elements(By.XPATH, '//div[contains(@class, "geS5n")]//span[contains(text(), "Option")]//ancestor::div[contains(@class, "geS5n")]//div[contains(@class, "Od2TWd hYsg7c")]')
                    option_tickboxes[row[col]].click()
                i+=1
            multiple_tickboxes = self.driver.find_elements(By.XPATH, '//div[contains(@class, "geS5n")]//span[contains(text(), "Multiple choices")]//ancestor::div[contains(@class, "geS5n")]//div[contains(@role, "checkbox")]')
            for i in range(0, 4):
                if random.randint(0, 1):
                    multiple_tickboxes[i].click()
            button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Gư')]/ancestor::div[contains(@role, 'button')]")
            button.click()
            time.sleep(1)

            
                
                


        

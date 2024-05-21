# selenium-related
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

# other necessary ones
import urllib.request
import json
import time
import re
import datetime
import multiprocessing

# from components folder
from components.form_filler import Form_filler
from components.functions import create_excel
from components.constants import EXCEL_FILE
from components.constants import FORM
from components.constants import TOTAL_ROWS


def main(excel_file, start, rows):
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    form_filler = Form_filler(driver)
    form_filler.fill_form(FORM, excel_file, start, rows)
    

if __name__ == "__main__":
    threads = []
    thread_num = 4
    create_excel(TOTAL_ROWS, EXCEL_FILE)

    rows_per_thread = TOTAL_ROWS // thread_num

    for i in range(thread_num):
        start = i * rows_per_thread
        rows = rows_per_thread if i < thread_num - 1 else TOTAL_ROWS - i * rows_per_thread
        thread = multiprocessing.Process(target=main, args=(EXCEL_FILE, start, rows))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
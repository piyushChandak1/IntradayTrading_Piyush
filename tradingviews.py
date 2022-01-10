import logging
import time

import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np


options = Options()
PATH = "D:\\DRIVERS\\chromedriver.exe"

options.add_argument("user-data-dir=C:\\Users\\Piyush chandak\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)


driver.maximize_window()

driver.get("https://in.tradingview.com/")
time.sleep(2)


# Login if not available
try:
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[3]/button[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[6]/div/span/div[1]/div/div/div[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input").send_keys("piyushchandak1601@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/input").send_keys("Piyush@1601")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/button/span[2]").click()
    time.sleep(5)
except:
    print("Login already completed")

try:
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div/article/div[2]/div/button/span").click()
except:
    print("Cookies already accepted")



driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div/div/button[1]").click()
time.sleep(1)

try:
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input").send_keys("RELIANCE" + Keys.RETURN)
except:
    print("SOMTIMNG BAD OCCURED")
time.sleep(1)

"""
At this point the main page of the  stock or asset will open.
If some error takes place then you can do this process again
"""
try:
    while True:
        x = driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[5]").text
        time.sleep(1)
        print(x)
except Exception as e:
    print("Error occured" + e)






time.sleep(10)

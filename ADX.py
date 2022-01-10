"""Since ADX does not predict Buy or sell this will return weather to buy or sell option contracts
Since this is based on option selling 1 means HIGH Volatility and 0 means low Volatility"""
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pickle
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np










class ADX:
    def __init__(self):
        self.data = []

    def decrease_size(self):
        self.data = self.data[len(self.data) // 2:]

    def decreasearray(self):
        if len(self.data) > 10000:
            self.decrease_size()

    def predict(self):
        if self.data[-1] > 20:
            return 1
        else:
            return 0

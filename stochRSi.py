"""This is a stostic RSI indicator used to predict a buy or a sell signal
1 means BUY
0 means HOLD/NO TRADE
-1 means SELL
Run the predict function of the class to predict the following.
It should have feed of continuous data to predict it.If if misses the data it will return -3
which means somthing is wrong.
"""


import pandas as pd
import datetime

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









class stochRSI:
    def __init__(self):
        self.data = []

    def decrease_size(self):
        self.data = self.data[len(self.data)//2:]

    def add_data(self, b, s):
        self.data.append([b, s])

    def predict(self):
        a = self.data[-1][0]
        b = self.data[-1][1]
        if 20 < a < 80 or 20 < b < 80:
            return 0
        if 0 <= a <= 20 and 0 <= b <= 20:
            if a > b:
                return 1
            else:
                return 0
        if 80 <= a <= 100 and 0 <= b <= 100:
            if b > a:
                return -1
            else:
                return 0
    def continue_trade(self, cur_pos):
        """if cur_pos is 1 means i am in long and -1 means short"""
        """Returns a value between 1 and 10. 1 means the trade is very bad and you should exit 
        and 10 means you """
        pass

    def decreasearray(self):
        if len(self.data) > 10000:
            self.decrease_size()




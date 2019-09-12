import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from components.searchComponent import searchComponent

class searchPage:
    def __init__(self,driver):
        self.driver = driver
        self.searchComp = searchComponent(self.driver)
    
    def searchFor(self,word):
        self.searchComp.searchBox.send_keys(word+"\n")

    def press_back(self):
        self.driver.press_keycode(4)

    
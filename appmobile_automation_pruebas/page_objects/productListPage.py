import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from components.productListComponent import productListComponent

class productListPage:
    def __init__(self,driver):
        self.driver = driver
        self.productListComp = productListComponent(self.driver)

    def clickItem(self,number):
        self.productListComp.listOfResults[number-1].click()

    def obtainProductName(self,number):
        productName = self.productListComp.listOfResultsName[number-1].text
        return(productName)

    def press_back(self):
        self.driver.press_keycode(4)

    
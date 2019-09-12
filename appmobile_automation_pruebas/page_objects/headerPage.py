import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from components.headerComponent import headerComponent

class headerPage:
    def __init__(self,driver):
        self.driver = driver
        self.headerComp = headerComponent(self.driver)

    def clickSearchButton(self):
        self.headerComp.searchButton.click()

    def clickCesta(self):
        self.headerComp.miCesta.click()

    
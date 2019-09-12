import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from components.productComponent import productComponent

class productPage:
    def __init__(self,driver):
        self.driver = driver
        self.productComp = productComponent(self.driver)

    def selectProductSize(self):
        length = len(self.productComp.sizeOptions)
        cuenta = 0
        sizenumber = 0
        for i in range(0,length):
            length = len(self.productComp.sizeOptions)
            if self.productComp.sizeOptions[i].get_attribute('data-talla-accion')=="1":
                cuenta = cuenta + 1
                if cuenta > 1:
                    sizenumber = i
                    break
        Talla = self.productComp.sizeOptions[sizenumber].text
        self.productComp.sizeOptions[sizenumber].click()
        return(Talla)

    def addToTheShoppingCart(self):
        self.productComp.addShopping.click()

    def press_back(self):
        self.driver.press_keycode(4)




















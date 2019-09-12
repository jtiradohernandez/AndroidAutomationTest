import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from components.cestaComponent import cestaComponent

class cestaPage:
    def __init__(self,driver):
        self.driver = driver
        self.cestaComp = cestaComponent(self.driver)

    def clickTramitarPedido(self):
        self.cestaComp.tramitarPedido.click()

    def obtainProductName(self,number):
        return(self.cestaComp.nombresProducto[number-1].text)

    def obtainTallaName(self,number):
        return(self.cestaComp.tallasProducto[number-1].text)

    

    
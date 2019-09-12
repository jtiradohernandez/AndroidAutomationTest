import os
import sys
import time
from behave import *
from appium import webdriver
from page_objects.cestaPage import cestaPage

@then('the "{number:d}" item on the basket is the same as you clicked')
def itemOnBasketIsCorrect(self,number):
    cesta = cestaPage(self.driver)
    productreal = cesta.obtainProductName(number)
    tallareal = cesta.obtainTallaName(number)
    assert productreal == self.productName
    assert tallareal == "Talla "+ self.Talla.strip()
    
if __name__ == '__main__':
    self.driver = webdriver.Remote()
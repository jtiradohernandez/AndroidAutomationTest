import os
import sys
import time
from behave import *
from appium import webdriver
from page_objects.headerPage import headerPage
from page_objects.cestaPage import cestaPage


@when('Click on Mi Cesta')
def whenClickCesta(self):
    headerPage(self.driver).clickCesta()

if __name__ == '__main__':
    self.driver = webdriver.Remote()
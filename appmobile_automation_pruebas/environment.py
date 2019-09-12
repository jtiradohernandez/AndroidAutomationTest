import os
import multiprocessing as mp
from time import sleep
from appium import webdriver
from variables import *

def before_all(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = 'PON AQUÍ EL SISTEMA OPERATIVO'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['browserName'] = 'Chrome'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['autoGrantPermissions'] = 'true'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def after_all(self):
    self.driver.quit()

def before_feature(self, feature):
    pass

def after_feature(self, feature):
    pass
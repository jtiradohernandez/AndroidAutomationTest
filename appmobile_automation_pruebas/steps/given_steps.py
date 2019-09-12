import os
import sys
import time
from behave import *
from appium import webdriver
from page_objects.headerPage import headerPage
from page_objects.searchPage import searchPage
from page_objects.productListPage import productListPage
from page_objects.productPage import productPage
from page_objects.cestaPage import cestaPage


@given('Go to Zatro.es')
def givenGoWebsite(self):
    self.driver.get('http://www.zatro.es')

@given('Click the search button')
def givenClickSearchButton(self):
    headerPage(self.driver).clickSearchButton()

@given('Search for "{word}"')
def givenSearchFor(self,word):
    time.sleep(5)
    searchPage(self.driver).searchFor(word)

@given('Click the item "{number:d}"')
def givenClickItem(self,number):
    productList = productListPage(self.driver)
    self.productName = productList.obtainProductName(number)
    productList.clickItem(number)

@given('Select the second available shoe size')
def givenSelectProductSize(self):
    self.Talla = productPage(self.driver).selectProductSize()

@given('Add it to the shopping cart')
def givenAddToTheShoppingCart(self):
    productPage(self.driver).addToTheShoppingCart()

@given('Click Tramitar Pedido')
def givenClickTramitarPedido(self):
    cestaPage(self.driver).clickTramitarPedido()

if __name__ == '__main__':
    self.driver = webdriver.Remote()
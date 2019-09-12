import sys

class headerComponent():

    def __init__(self,driver):
        self.driver = driver

        #Direcciones
        self.searchButtonCSS = 'div.header nav.menu-container div.JS-buscar-btn.buscar-btn'
        self.miCestaClass = 'cesta-btn'

        #Elementos Web
        self.searchButton = self.driver.find_element_by_css_selector(self.searchButtonCSS)
        self.miCesta = self.driver.find_element_by_class_name(self.miCestaClass)
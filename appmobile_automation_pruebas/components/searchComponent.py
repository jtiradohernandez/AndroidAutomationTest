import sys

class searchComponent():

    def __init__(self,driver):
        self.driver = driver

        #Direcciones
        self.searchBoxCSS = 'iBuscar'
  
        #Elementos Web
        self.searchBox = self.driver.find_element_by_class_name(self.searchBoxCSS)
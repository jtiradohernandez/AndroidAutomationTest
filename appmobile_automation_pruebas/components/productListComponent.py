import sys

class productListComponent():

    def __init__(self,driver):
        self.driver = driver

        #Direcciones
        self.listOfResultsClass = 'product'
        self.listOfResultsNameClass = 'nombre'
        
        #Elementos Web
        self.listOfResults = self.driver.find_elements_by_class_name(self.listOfResultsClass)
        self.listOfResultsName = self.driver.find_elements_by_class_name(self.listOfResultsNameClass)
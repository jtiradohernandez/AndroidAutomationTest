import sys

class productComponent():

    def __init__(self,driver):
        self.driver = driver

        #Direcciones
        self.sizeOptionsClass = 'variante'
        self.addShoppingCSS = 'div.cont-botones button.add-cart'

        #Elementos Web
        self.sizeOptions = self.driver.find_elements_by_class_name(self.sizeOptionsClass)
        self.addShopping = self.driver.find_element_by_css_selector(self.addShoppingCSS)

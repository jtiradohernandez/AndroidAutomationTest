import sys

class cestaComponent():

    def __init__(self,driver):
        self.driver = driver

        #Direcciones
        self.tramitarPedidoCSS = 'a.btn-pagar'
        self.nombresProductoClass = 'titulo'
        self.tallasProductoClass = 'talla'

        #Elementos Web
        self.tramitarPedido = self.driver.find_element_by_css_selector(self.tramitarPedidoCSS)
        self.nombresProducto = self.driver.find_elements_by_class_name(self.nombresProductoClass)
        self.tallasProducto = self.driver.find_elements_by_class_name(self.tallasProductoClass)
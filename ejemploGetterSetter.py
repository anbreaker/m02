class ClaseConGetterSetter():
    def __init__(self):
      self.__propiedad_privada = None
    
    #Getters
    def getPropiedadPrivada(self):
        return self.__propiedad_privada

    #Setters
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor

    #Getters y Setters Juntos
    def propiedadPrivada(self, valor = None):
        #Actuacion del Getter
        if valor == None:
            return self.__propiedad_privada
        #Actuacion del Setter
        else:
            self.__propiedad_privada = valor
            
    
    def __str__(self):
        return "ClaseConGetterSetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    

if __name__ == '__main__':
    c = ClaseConGetterSetter()
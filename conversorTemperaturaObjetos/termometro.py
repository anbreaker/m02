#Objeto

#-------------------#
#     Termometro    #
#-------------------#
#  - unidad(C,F)    #
#  - temperatura    #
#-------------------#
#  - conversor(T,U) #
#  - get y set      #
#-------------------#

class Termometro():
    def __init__(self):
      self.__unidad = 'C'
      self.__temperatura = 0

    def conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{} ºF ".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{} ºC ".format((temperatura - 32) * 5/9)
        else:
            return 'Unidad incorrecta'
    
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidad)


    def unidadMedida(self, unidadM = None):
        if unidadM == None:
            return self.__unidad
        else:
            if unidadM == 'F' or unidadM == 'C':
                self.__unidad = unidadM
    
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
    
    def mide(self, uniM=None):
        if uniM == None:
            return self.__str__()
        else:
            return self.conversor(self.__temperatura, self.__unidad)


def main():
    c = Termometro()
    print(c.conversor(0, 'C'))
    print(c.conversor(32, 'F'))
    
main()

''' Pruebas
t = Termometro()
t.temp(32)
t.unidadMedida('F')
t.mide()
'''
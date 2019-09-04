#Objeto

#-------------------#
#     Termometro    #
#-------------------#
#  - unidad(C,F)    #
#  - temperatura    #
#-------------------#
#  - conversor(T,U) #
#-------------------#

class Termometro():
    def __init__(self):
      self.unidad = 'C'
      self.temperatura = 0

    def conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{} ºF ".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{} ºC ".format((temperatura - 32) * 5/9)
        else:
            return 'Unidad incorrecta'
    
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidad)

def main():
    c = Termometro()
    print(c.conversor(0, 'C'))
    print(c.conversor(32, 'F'))
    
main()

class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None

    def ladrar(self):
        if self.peso == None:
            print('Soy un fantasma')
        
        if self.peso >= 8:
            print('Soy un fantasma')
        else:
            print('guau, guau')


class Perro():
    def __init__(self, nombre, edad, peso):
      self.nombre = nombre
      self.edad = edad
      self.peso = peso

    def ladrar(self):
        if self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print('guau, guau')

    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)


class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        return "Perro de asistencia {},".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.trabajando != True:
            print("ssshhhhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

    

salchicho = Perro('salchicho',3,12)
lola = Perro('lola',8,1.5)
rantan = Perro('miko',8,3)
miko = PerroAsistencia('Milú', 4, 8,'Lucky Luke')

#rantanplan.ladrar()
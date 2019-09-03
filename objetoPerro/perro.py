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
    
    

salchicho = Perro('salchicho',3,12)
lola = Perro('lola',8,1.5)
miko = Perro('miko',8,3)
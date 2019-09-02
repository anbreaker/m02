def maximo(*l):
    if len(l) == 0:
        return 0
    m = l[0]

    for ix in range(1,len(l)):
        if l[ix] > m:
            m = l[ix]
    return m
    
def minimo(*l):
    if len(l) == 0:
        return 0
    m = l[0]

    for ix in range(1,len(l)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(l) == 0:
        return 0

    suma = 0
    
    for valor in l:
        suma += valor
    return suma / len(l)

funciones = {
    'max': maximo,
    'min':minimo,
    'med':media
}

def returnF(nombre):
    if nombre.lower() in funciones.keys():
        return funciones[nombre]

    return None


maximo(-2,3,5,9,-3,19,-33)
minimo(-2,3,5,9,-3,19,-33)
media(-2,3,5,9,-3,19,-33)

returnF('max')
returnF('max')(1,3,-1,15,9)
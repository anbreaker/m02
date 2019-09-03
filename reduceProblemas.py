from functools import reduce

def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += r
    return resultado

def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
    return resultado

def productoTotal(l):
    resultado = 0
    for valor in l:
        resultado *= valor
    return resultado

lista = [1, 3, -1, 15, 9]

sumatorioReduce = reduce(lambda x, y: x + y, lista)

#creo unacopia de la lista
l = lista[:]
#añado el neutro para la suam en la posicion 0
l.insert(0,0)
sumatorioDobleReduce = reduce(lambda x, y: x + y * 2, l)

print(sumatorioReduce)
print(sumatorioDobleReduce)
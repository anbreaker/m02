from functools import reduce

lista = [1, 3, -1, 15, 9, 8]

listaDobles = map(lambda x: x*2, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)

sumatorio = reduce(lambda x, y: x + y, lista)

sumaCien = reduce(lambda x,y: x + y, range(101))
from funcionesPrimerNivel import sumaTodos

doble = lambda x: x**3

print(sumaTodos(3, doble))

print(sumaTodos(3, lambda x: x * 2))
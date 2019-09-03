from funcionesPrimerNivel import sumaTodos

doble = lambda x: x**3


if __name__ == '__main__':
    print(sumaTodos(3, doble))
    print(sumaTodos(3, lambda x: x * 2))

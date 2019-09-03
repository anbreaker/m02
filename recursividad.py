def retroContador(entrada):
    print("{}".format(entrada), end='\n')
    if entrada > 0:
        retroContador(entrada -1)

def sumatorioRecursivo(n):
    #print("{}".format(n), end='\n')
    if n > 0:
        return n + sumatorioRecursivo(n-1)
    else:
        return 0 #4+3+2+1+0
    
def factorialRecursivo(n):
    if n > 0:
        return n*factorialRecursivo(n-1)
    else:
        return 1
    

print('Factorial: ', factorialRecursivo(4))
print('Sumatorio Recursivo: ', sumatorioRecursivo(4))
print('\nRetrocontador: ')
retroContador(10)

#4+sumatorioRecursivo(3)
#4+3+sumatorioRecursivo(2)
#4+3+2+sumatorioRecursivo(1)
#4+3+2+1+sumatorioRecursivo(0)
#4+3+2+1+0
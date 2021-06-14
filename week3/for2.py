#
#Desarrollar un programa que solicite la carga de 10 números
#e imprima la suma de los últimos 5 valores ingresados.
#

def for_exercise2():
    lista = []
    
    for i in range(10):
        lista.append(int(input('inserte un numero: ')))
    
    sum = 0
    for i in range(4, 10):
        sum += lista[i]
    
    return sum

print(for_exercise2())
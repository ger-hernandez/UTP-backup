#Desarrollar un programa que permita cargar n números enteros
#y luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura
#condicional (este operador retorna el resto de la división de dos valores
#,por ejemplo 11%2 retorna un 1): if valor%2==0:

def while_exercise7(list:list):
    par = impar = i = 0
    while i < len(list):
        if list[i] % 2 == 0:
            par += 1
        else:
            impar += 1
        i += 1
    
    print(f'there were {par} even items in the list')
    print(f'there were {impar} odd items in the list')
    return 1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

while_exercise7(lista)
    
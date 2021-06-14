# Confeccionar un programa que lea n pares de datos,
# cada par de datos corresponde a la medida de la base y la altura de un triángulo.
# El programa deberá informar: a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

# lista = []
# n1 = input()
# n2 = input()
# lista.append([n1, n2])
# lista.append([n1, n2])
# print(lista)

def for_exercise1():
    
    
    lista_triangulos = []
    n = int(input('how may triangles are you doing today? '))

    for i in range(n):
        base = int(input(f'Inserte base del triangulo {i + 1}: '))
        altura = int(input(f'Inserte altura del triangulo {i + 1}: '))
        lista_triangulos.append([base, altura, base * altura / 2])

    print(lista_triangulos)

    mayor_12 = 0

    i = 1
    
    for x in lista_triangulos:
        y = 0
        print('------------------------------------------------')
        print(f'la base del triangulo {i} is {x[y]}')
        print(f'la altura del triangulo {i} is {x[y + 1]}')
        print(f'la superficie del triangulo {i} is {x[y + 2]}')
        i += 1
        if (x[ y + 2] > 12):
            mayor_12 += 1
        

    print(f'there are {mayor_12} triangles whose superfice is grather than 12.')   
    return 1

for_exercise1()


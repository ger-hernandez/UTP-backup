# Realizar un programa que permita cargar dos listas de 15 valores cada una.
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") 
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

def while_exercise6(list, list2):
    if not(len(list) == 15 and len(list2) == 15):
        print('lists must be 15 items long')
        return 1
    
    sum1 = sum(list)
    sum2 = sum(list2)

    if( sum1 > sum2):
        print('list 1 is major')
    elif(sum2 > sum1 ):
        print('list 2 is major')
    else:
        print('list are equal')
    
    return 1
   
    

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]
items2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while_exercise6(items, items2)
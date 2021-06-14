#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar
# del mismo (los primeros 12 términos)
def for_exercise4():
    op1 = 0
    
    while True:
        op1 = int(input('ingrese un numero del 1 al 10: '))
        if not(op1 <= 0 or op1 > 10):
            break
        else:
            print('El numero debe estar entre 1 y 10!')

    for i in range(1, 13):
        print(f'{op1} x {i} = {op1 * i}')
    
    return 1

for_exercise4()

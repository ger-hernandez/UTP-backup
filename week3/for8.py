# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.


def carga_num():
    nums = []
    for i  in range(10):
        x = int(input('Ingrese un numero: '))
        nums.append(x)
    
    neg = pos = mul15  = par = 0

    for num in nums:
        if(num < 0):
            neg += 1
        elif(num > 0):
            pos += 1
        if( num % 15 == 0):
            mul15 += 1
        if(num % 2 == 0):
            par += num
    print(f'la cantidad de valores negativos es {neg}')
    print(f'la cantidad de valores positivos es {pos}')
    print(f'la cantidd de valores  que son multiplos de 15 son {mul15}')
    print(f'la sumatoria de los numeros pares es{par}')
    return 1

carga_num()

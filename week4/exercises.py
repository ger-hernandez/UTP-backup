# from functools import reduce
# import math
# #Utilizar la función incorporada map() para crear una función que retorne una lista con la 
# #longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena 
# #de texto y retornará una lista

# def longitud_frase(s):
#     s = s.split(' ')
#     return list(map(len, s))

# s = 'h ol are'
# #print(longitud_frase(s))

# #Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
# #Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función  reduce

# def list_digits(n):
#     n = [str(x) for x in n]
#     return reduce(lambda a, b: a + b, n)

# n = [3, 6, 9]
# #print(list_digits(n))

# #Crear una función que retorne las palabras de una lista de palabras que comience con una 
# #letra en específico. Utilizar la función filter
# def filter_letter(l:list, c:str):
#     return list(filter(lambda x:x[0].lower() == c.lower(), l))

# l = ['carro','casa','german', 'Charco']
# #print(filter_letter(l, 'G'))

# #Realizar una función que tome una lista de comprensión para devolver una lista de la misma
# #longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre
# #ellas. Ejemplo: Listas: ['A', 'a'] ['B','b'] Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función
# #zip

# def conca(l1, l2, cone):
#     return [x + cone + y for (x, y) in zip(l1, l2)]

# l1 = ['A', 'a']
# l2 = ['B', 'b']
# l3 = conca(l1, l2, '-')

# #print(l3)

# #Realizar una función que tome una lista y retorne un diccionario que contenga los valores de
# #la lista como clave y el índice como el valor. Utilizar la función enumerate.

# def lista_dict(l:list):
#     return {x:y for x, y in enumerate(l)}

# neo_dict = lista_dict(['one', 'two', 'three'])

# #Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo
# #valor es igual a su índice. Utilizar la función enumerate.

# def recuento(l):
#     return len([y for x,y in enumerate(l) if x == y])

# lx = [2, 1, 7, 3, 5]
# #print(recuento(lx))

# var = ['yes', 'no'][0]

# #print(var)

# # Input: 42145 Output: 54421

# # Input: 145263 Output: 654321

# # Input: 123456789 Output: 987654321

# def descending_order(num):
#     num = [int(x) for x in str(num)]
#     new_num = []
#     while len(num) > 0:
#         g = max(num)
#         new_num.append(str(g))
#         num.remove((g))
    
#     return int("".join(new_num))

# #print(descending_order(42145))

# def end_zeros(num: int) -> int:
#      l = str(num)
#      c = 0
#      for x in l:
#          if x == '0':
#              c += 1    
#      return c

# #print(end_zeros(10))

# x = 1000
# for y in range(17):
#     x += math.floor(x * 0.08)

# x+= math.floor(x * 0.07)

# for y in range(2):
#     x += math.floor(x * 0.08)


# #print(x)
# #delete duplicate letters case insensitive
# def duplicate_count(s:str):
#     counter = 0
#     s = list(s.lower())
#     for index, value in enumerate(s):
#         if(s.count(value) > 1):
#             counter += 1
#             for x in range(index + 1, len(s) - 1 ):
#                 if(s[index] == s[x]):
#                    s.pop(x)
#     # for  value in s:
#     #     if(s.count(value) > 1):
#     #         counter+=1
#     #         for x in s:
#     #             if (x == value):
#     #                 print(f'{x}', end=' ')
#     #                 s.remove(x)
#     return counter
# #TODo
# #print(duplicate_count('fj9rShHjXcPDrKGTt9qO25d8UQTDM'))
# num = 9119
# def square_digits(num):
#    l = [int(x) ** 2 for x in str(num)]
#    return int("".join([str(x) for x in l]))

# def square_digits2h(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))

# #print(square_digits(num))

# d = {

# }
# digit = 1

# d['p{digit}'] =  12

# #print(d)

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
i = 0
total = 0
while(i <  len(given_list)):
    if(i < 0):
        total += given_list[i]
    i += 1
print(total)

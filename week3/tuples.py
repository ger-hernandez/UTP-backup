#tuples are inmutable elements
t = (1, 2, 3, 4, 5) #tuple example
#we can acces a tuple with square bracket notation
t[0] # 1
#to create a tuple with just one elemente just must add a coma to the end
t2 = ('a',) #one element tuple
#to create an empty tuple
t3 = tuple()
#if the element inside the constructor is an iterable the constructor splits the elements
#slicing
t[:3] #(1, 2, 3)
#tuples cant be modified
#we can have tuples to the left for assignacion
l = [2, 1]
a, b = l
# print(a, b)
correo = 'gerhernandez7@gmail.com'
name, mail = correo.split('@', 2)
# print(name)
# print(mail)

d = {'a':10, 'b':1, 'c':22}
t = sorted(list(d.items()), reverse=True)
print(t)

diccionario = {}
apellido = 'hernandez'
nombre = 'german'
numero = '39438489234'
diccionario[nombre, apellido] = numero
print(diccionario)
print(diccionario[nombre, apellido])
#metodo count() returns a count of the ocurrences
#metodo index() returns index of element



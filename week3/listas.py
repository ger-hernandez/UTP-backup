lista = [1, 2.5, 'DevCode', [5,6], 4, 4] #lists can contain different data types
#we can acces lists with square bracket notatio
lista[1] # => 2.5
#slice a list
lista[:2] #=> [1, 2.5]
lista2 = lista[:] #copying a list
lista3 = lista[::2] # [1, 'devcode', 4]
lista[-1] #last position of the list '4'
len(lista) #n elements of the list 4
#append, appends an element to the end of the list
lista.append(10)
#lista.clear() deletes all elements from the list

lista4 = lista.copy() # creates a copy of the list, the same as list[:]
lista.count(4) # returns the n ocurrences of the item '2'
lista.extend((x for x in range(5))) #extends a list with an iterable

lista.index(4) #finds the item of the first ocurrence oof the item passed
lista.insert(2, 'german') #inserts object before the index

popped = lista.pop(lista.index(0)) #pops element with the index specified
lista.remove(4) #remove the first ocurrence with the specified value
#print(lista)

#lista.reverse() #reverse a list
lista6 = lista[::-1] #also reverse a list
# print(lista6)
# print(list(reversed(lista6)))
numeric = list(range(6))
numeric.sort(reverse=True)
print(numeric)
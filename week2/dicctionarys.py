from typing import Iterator, Generator, Tuple
dicto = {}
dicto["nota_1"] = 4
dicto["nota_2"] = 5
dicto["nota_3"] = 2

def promedio(dicto):
    return sum(dicto.values()) / len(dicto.values())

#print(promedio(dicto))

#print(dicto)
#dicto.clear() => removes all items from the dictionary
dicto_2 = dicto.copy()
# print(dicto_2)
# print(dicto is dicto_2)
# print(dicto == dicto_2)
# dict_b = dicto
# print(dicto is dict_b)
# print(dicto == dict_b)
# print(id(dicto))
# print(id(dict_b))
# dict_b['name'] = 'german'
# print(dicto)
dicto_keys = dicto.keys() #=> a set like object with the key
dicto_values = dicto.values() #=> a set like object with the values

secuence = ('drake', 'lil_wayne', 'migos')
dictionary = dict.fromkeys(secuence, [1]) #creates a dictionary with the keys in secuence
dictionary['drake'].append(2)
#print(dictionary)

#dictionary comprehension
vowels_key = (x for x in 'aeiou')
value = [1]
vowels = {x : value[:] for x in vowels_key}
#print(vowels)
vowels['a'].append(2)
#print(vowels)

#get
dicto.get('nota_2') #=> returns 5, if the keys doesnt exist returns None
#print(dicto.get('nota_4') == None)

#items
dicto.items() #=> a set like object providing a view o d's items, key : value pairs
#pop
vowels.pop('a') #pops the item, it has a second argument with a default value
#update
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones.update(y =0, d = 1)
print(versiones)
#updates the dict to new items or can modify an item
#len of a dictionary
print(len(versiones))
#popitem
#removes the last item of the dictionary
versiones.popitem() #removes d:1 from versiones
print(versiones)
#versiones.setdefault(key, default) #returns the value if the key exist else inserts the key value pair
#del
#removes an key,value pair from the dictionary and doesn't return shit
del versiones['zope'] #deletes zope from versiones
print(versiones)

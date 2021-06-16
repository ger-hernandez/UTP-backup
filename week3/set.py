#to create a set
my_set = {1, 2, 3, 4}
#can be diverse
lgbt_set = {1, 'hola', 2.5, True}
#to create an empty set
empty_set = set()
#if we turn list, or any iterable to a set repeated characters
#will be deleted even chars in a string
#to acces elements in a set we need to use loops, since
#sets are unordered objects they cn be accesed through indexes
#methods
# set.add('x') #adds an element to a list
# set.clear() #removes all elements from the list
# set.copy() #shallow copy of a set
print(my_set.difference([1, 2, 3])) #the items that are in myset that arent in the iterable
proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
proyecto2 = {'python', 'Plone', 'diazo'}
proyecto1.difference_update(proyecto2) #deletes the items that are in proyecto 2 from proyecto 1
print(proyecto1)
#set.discard('x') #removes element from the set if found
#set.intersection(set2) #returns a new set with the intersection of the two sets
#set.intersection_update(set2, set 3)  updates set1 with the intersection between self and the arguments]
#set.isdisjoint()
set_mutable1 = set([4, 3,  7,  1, 4])
set_mutable2 = set([ 5, 9, 2,  8])
print(set_mutable1.isdisjoint(set_mutable2)) #true cuz they don have similar objects
#set.issubset(set2) returns True is all elements of set are in set2
#set.issuperset(set2) returns true if all of set2 are in set
#set.pop() deletes a random element from the set, the set is updated an the element is returned
#set.remove('x') remove x if found in set
#set.symmetric_difference(b) returns the items that are in in set a but not in b and viceversa
#set.symmeticr_difference_update(x) updates a with the symetric difference btewen set and x
#set.union(set1, set2...) unifys all the elements of the set
#set.update(iterable) updates the element with the items in the iterable
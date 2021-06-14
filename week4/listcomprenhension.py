#an elegant way of making list
numbers = [x for x in range(10)]
print(numbers)

#we can even get data from other lists and apply operations
power = [x ** 2 for x in numbers]
print(power)

#we can even use conditionals
even = [x for x in numbers if(x % 2 == 0)]
print(even)

#applyfunctions
fruits = ['banana', 'apple', 'mango']
printing =[ print(x) for x in fruits]

#callingmethods
up = [x.upper() for x in fruits]
print(up)

#creating tuples from a list
pairSquare = [(x, x**2) for x in numbers]
print(pairSquare)
print(f'{[type(x) for x in pairSquare]}')

#creating tuples and dictionaries with list comprenhension
tp = tuple(x**2 for x in numbers) #we need the tuple object creator
print(tp)

dc = {x : x**3 for x in numbers}
print(dc)

#from string to dicc
hey = 'hola'
di_hey = dict(enumerate(hey))
print(di_hey)


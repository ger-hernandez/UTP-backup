# #an elegant way of making list
# numbers = [x for x in range(10)]
# print(numbers)

# #we can even get data from other lists and apply operations
# power = [x ** 2 for x in numbers]
# print(power)

# #we can even use conditionals
# even = [x for x in numbers if(x % 2 == 0)]
# print(even)

# #applyfunctions
# fruits = ['banana', 'apple', 'mango']
# printing =[ print(x) for x in fruits]

# #callingmethods
# up = [x.upper() for x in fruits]
# print(up)

# #creating tuples from a list
# pairSquare = [(x, x**2) for x in numbers]
# print(pairSquare)
# print(f'{[type(x) for x in pairSquare]}')

# #creating tuples and dictionaries with list comprenhension
# tp = tuple(x**2 for x in numbers) #we need the tuple object creator
# print(tp)

# dc = {x : x**3 for x in numbers}
# print(dc)

# #from string to dicc
# hey = 'hola'
# di_hey = dict(enumerate(hey))
# print(di_hey)
# Y = 10
# my_dict = {(x,  x ** 2) : x  for x in range(1, 11) }
# print(my_dict)
# print(my_dict[6, 36])

#comprehension... lists, set, tuples, dict
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #n for each n in nums with  a for loop
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

#now with list comprehension
my_list2 = [n for n in  nums] #one liner, beautiful
#now a example with expressions
#square_list
my_list3 = [n*n for n in nums] # a list with n square
print(nums, my_list2, my_list3)



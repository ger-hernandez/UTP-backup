from functools import reduce
#In mathematics and computer science,
#  a higher-order function is a function that does at least one of the following:
#  takes one or more functions as arguments, returns a function as its result.

#map function
numbers = [2, 4, 8]
#def sq(n):
    #return n * n

#square = list(map(sq, numbers))
squareL = list(map(lambda x: x * x, numbers))
print(squareL)

#square2 = [ sq(n) for n in numbers]
#print(square2)

#experimenting with map and lambda
plus = list(map(lambda x : x **3, [2, 3, 4] ))
print(plus)

#filter
#we can filter an object with the elementes that meet our conditions
#example with external function
def is_vowel(c):
    return c.lower() in 'aeiou'

letters = ['a', 'c', 'd', 'e', 'p']
vowels = list(filter(is_vowel, letters))
print(vowels)

#with lambda
numbers = [ x for x in range(1, 11)]
#print(numbers)
#filter even numbers using lambda
even = list(filter(lambda x : x % 2 == 0, numbers))
#print(even)
odd = list(filter(lambda x: x % 2 != 0, numbers))
#print(odd)

#reduce 
sumatoria = reduce(lambda x, y: x + y, numbers)
#print(sumatoria)

#delete duplicate letters case insensitive
def duplicate_count(s:str):
    counter = 0
    s = list(s.lower())
    for  value in s:
        if(s.count(value) > 1):
            counter+=1
            for x in s:
                if (x == value):
                    print(f'{x}', end=' ')
                    s.remove(x)
    return counter

print(duplicate_count('fj9rShHjXcPDrKGTt9qO25d8UQTDM'))
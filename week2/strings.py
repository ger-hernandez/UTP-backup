fruit = "Strawberry"
letter_1 = fruit[0]
l = len(fruit) #long of the str
final_letter = fruit[-1] #last letter of the str 'y'

#slicing strings
straw = fruit[:5] #straw
berry = fruit[5:] # berry
fruit_cp = fruit[:] #=> a copy of the fullstring 

'tr' in fruit_cp # true cuz 'tr' is a substring of fruit_cp
#in verifies that something is part of an object
'st' not in fruit # true cuz 'st' is not in fruit

dir(fruit) #prints all the methods of an object

#managing case
#help(str.capitalize) # prints information about the method in ()
fruit.casefold() # lowercase a string
fruit.upper() # => STRAWBERRY
fruit.lower() # => strawberry

#find the index of a substring
index_of_r = fruit.find('r') # => returns de index of the first 'r' in the string
#finding the index of a substring with a start position
index_of_r2 = 0
if ('r' in fruit):
    index_of_r2 = fruit.find('r', index_of_r + 1)
    
#centering a string
title = "Title"
str_to_center = "Title".center(20, '-')
# print(title) => title
#print(str_to_center) => ------Title-----

#return number of ocurrences of a substring - admidts start and end arguments
ocurrences_of_r = fruit.count('r')
print(ocurrences_of_r)

#encoding
fruitutf8 = fruit.encode(encoding='utf-8', errors='strict')

fruit.endswith('ry') #=> True cuz fruit ends with 'ry' admits start and end
fruit.startswith('St') #=> True cuz fruit starts with St

#str.expandtabs( tabsize = x) => returns a copy of the string where all tab char aare replalced with spaces
#str.format
#print('Hello I\'m {} years old and my name is {}'.format(29, 'German'))
#=> Hello I'm 29 years old and my name is German

#str.format_map() => return a string with the values of a dict 

#str.index(substring, star, end) => finds the index of a substring similar to str.find()

'12345abcd'.isalnum() #=> True cuz numbers are alphanumeric 
#if isdigit(), isnumeric(), isalpha(), and isdecimal() are True 
'german'.isalpha() #=> True cuz all chars are letters
'g23j'.isascii() #=> True cuz all chars are ascii
'1'.isdecimal() #=> returns True if the string is a number is a number base 10
'12'.isdigit() #=> True cuz the string is a number

'abcd'.islower() #=> true cuz all the letters are lowcase
'ABCD'.isupper() #=> True cuz all the chars are upper case
'12'.isnumeric() #=> True if all the chars are numeric
#str.isprintable() #=> returns true if the character is printable

' '.isspace() #=> True cuz the string is a space
'Title Llo'.istitle() #=> True cuz the string is capitalized

' '.join(['banana', 'apple', 'pear']) #=> 'banana apple pear'

#str.ljust(width, fillchar) #=> returns the string left justified
'  title '.lstrip() #=> remove the spaces character at the left
' aaaaamamamannaka '.lstrip('an') #=> mamannaka
#str.maketrans() and str.translate()
s = 'abcdefghiabcdefghi'
d = str.maketrans('aei', 'eio') #maaps the chars in the left to be replaced for the ones in the right
#turns the letters into  dict ascii values 
new_string = s.translate(d) #implements the mapping
#str.maketrans has a third arguments that removes characters from the string
#str.partition(arg) splits the string in a tuple with three parts the arg must be a separator
#str.removeprefix(prefix)
#removes the prefix in the string if the prefix exists in the string
'german'.removeprefix('ger') #=> man
#is the same as str[len(prefix):]
'german'.removesuffix('man') #=> ger
'aeiaeiaei'.replace('a', 'b') #=? replaces the first argument with the second, the third argument specifies how many ourrences of the char will be replaced
#str.rfind('c') => returns the highest index of the ocurrence
string = 'abca'
string.rfind('a') #=> 3
#str.rstript() removes whitespaces at the right
#str.rindex is the same as rfind but raises valueerror
#str.rjust(width) justifies string to the left
#str.rpartition(sep) split the string at the last ocurrence
#str.rsplit(sep, maxplit)
#returns a list of the string, starting from the right default separator is space
'hola soy german'.rsplit() #=> ['hola', 'soy', 'german']
#str.split() like rplit but start fromt the left
#str.splitlines(keepends) returns a list of the lines breakig at the line breaks
#str.strip() removes all whitespaces
#str.swapcace() swaps the cases of the letters
#str.title() => returns a titlecase of the string basiclly the first letter of each word gets uppercased
#str.zfill() fills the string at the left with ascii 0s







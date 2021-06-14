
try:
    r = 4/0
except ZeroDivisionError as error:
    #print('you can\'t divide by zero')
    print(error)
except NameError as error:
    #print('Can\'t you name a variable right?')
    print(error)
else:
    r += r
finally:
    print(r)


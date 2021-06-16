#while
l = [x for x in range(5)]
i = 0
while(i < len(l)):
    print(l[i])
    if( i == 6):
        break
    i += 1
else:
    print('not found') #doesn't make sense to have else if theres'nt a break

for x in l:
    if(x == 3): #will skip the 3
        continue
    print(x)
else:
    print('the loop has finished') #this always prints unless there is a break statement

for x, y in enumerate(l):
    print(x, y)
    print(type(x), type(y))
    
z = tuple([x, y] for x, y in enumerate(l))
print(z)

#fibonacci
a, b = 0, 1
while b < 100:
    print (b)
    a, b = b, a + b
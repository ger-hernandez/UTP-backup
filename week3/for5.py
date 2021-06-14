#Realizar un programa que lea los lados de n triángulos,
#e informar: a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
#isósceles (dos lados iguales),
#o escaleno (ningún lado igual) 
# b) Cantidad de triángulos de cada tipo.

#triangulo equilatero: todos sus lados son iguales
#triangulo isosceles: two sides of the same length
#triangulo escaleno: all the lengths are diferent

def is_eq(a, b, c):
    if (a == b and b == c):
        return True
    else:
        return False

def is_iso(a, b, c):
    if(a == b and a != c):
        return True
    if(a == c and b != c):
        return True
    if(b == c  and b != a):
        return True
    return False

def is_sc(a, b, c):
    if (a != b and a != c and b != c):
        return True
    else:
        return False

def for_exercise5(t):
    a = b = c = 0
    iso = eq = sc = 0
    for x in t:
        for y in range(1):
            a = x[y]
            b = x[y + 1]
            c = x[y + 2]
            if(is_eq(a, b, c)):
                eq += 1
                print(f'el triangulo de medidas {x}: es Equilatero')
            if(is_iso(a, b, c)):
                iso += 1
                print(f'el triangulo de medidas {x}: es Isosceles')
            if(is_sc(a, b, c)):
                sc += 1
                print(f'el triangulo de medidas {x}: es Escaleno')
    print(f'Hay {iso} triangulos isosceles, {eq} equilateros y {sc} escalenos.')
    return 1


triangulos = [[5, 5, 5,], [2, 4, 4,], [5, 6, 9], [3, 3, 6]]

print(for_exercise5(triangulos))

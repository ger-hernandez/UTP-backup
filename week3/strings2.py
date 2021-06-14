#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
#  Contar la cantidad de vocales.
#  Crear un segundo string con toda la oración en minúsculas para que sea más fácil
#  disponer la condición que verifica que es una vocal.

def is_vowel(c):
    return c.lower() in 'aeiou'

def n_vowels(s):
    n = 0
    for x in s:
        if(is_vowel(x)):
            n += 1
    
    return f'la oracion tiene {n} vocales.'

print(n_vowels('albert guerrillero hijueputa'))


# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

def white_spaces(s:str):
    w = 0
    for x in s:
        if(x.isspace()):
            w += 1
    
    return(f'la oracion tiene {w} espacios en blanco.')

print(white_spaces('mi nombre es german.'))
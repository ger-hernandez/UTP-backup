#
#Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
#controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido,
# en caso contrario mostrar un mensaje de error.

def clave():
    c = input('ingrese una clave entre 10 y 20 caracteres de largo: \n')
    if len(c) < 10 or  len(c) > 20:
        print('Ingresa bien esa monda care verga no sabes contar es animal!')

clave()


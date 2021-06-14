#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

def coordenadas(lista:list):
    x = 0
    y = 0
    cua_1 = cua_2 = cua_3 = cua_4 = 0
    for i in lista:
        x = i[0]
        y = i[1]
        if(x > 0 and y > 0):
            cua_1 += 1
        elif(x < 0 and y > 0 ):
            cua_2 += 1
        elif(x < 0 and y < 0):
            cua_3 += 1
        else:
            cua_4 += 1
    
    print(f'el cuadrante 1 tiene {cua_1} punto(s).')
    print(f'el cuadrante 2 tiene {cua_2} punto(s).')
    print(f'el cuadrante 3 tiene {cua_3} punto(s).')
    print(f'el cuadrante 4 tiene {cua_4} punto(s).')
    return  1

l = [[2, 5],[-2, 4],[-4, -2],[3, -2],[-1, 4]]

coordenadas(l)
# Se cuenta con la siguiente información: Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde. 
# Las edades de 11 estudiantes del turno noche. 
# Las edades de cada estudiante deben ingresarse por teclado. 
# a) Obtener el promedio de las edades de cada turno (tres promedios) 
# b) Imprimir dichos promedios (promedio de cada turno) 
# c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio de edades mayor.

def edades():
    lm = la = ln = []
    sm = sa = sn = 0

    for i in range(1, 6):
        e = int(input(f'inserte edad del estudiante {i} de la manana: '))
        lm.append(e)
        sm += e

    pm = sm / 5
    
    for i in range(1, 7):
        e = int(input(f'inserte edad del estudiante {i} de la tarde'))
        la.append(e)
        sa += e

    pa = sa / 6

    for i in range(1, 12):
        e = int(input(f'inserte edad del estudiante {i} de la noche'))
        ln.append(e)
        sn += e
    
    pn = sn / 11

    print(f'el promedio de la jornada manana es {pm}')
    print(f'el promedio de la jornada tarde es {pa}')
    print(f'el promedio de la jornada noche es {pn}')

    maximun = max(pm, pa, pn)

    if maximun == pm:
        print('la jornada con el promedio de edad mas alto es la manana')
    elif maximun == pa:
        print('la jornada con el promedio de edad mayor es la tarde')
    else:
        print('la jornada con el promedio de edad mas alto es la  noche')
    
    return 1

edades()
    

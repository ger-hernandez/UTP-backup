# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal

def while_exercise3(d:dict):
    less = more  = suma = 0

    i = 1
    l = len(d) 
    while(i <= l):
        if(d[i]['pay'] < 300):
            less += 1
        else:
            more += 1
        suma += d[i]['pay']
        i += 1

    print(f'La cantidad de empleados que gana menos de $300 es {less} \n y los que ganan mas de $300 son {more}')
    print(f'el importe de todos los salarios es {suma}')
    return 1

empleados = {
    1 :{
        'name' : 'german hernandez',
        'pay' : 500,
        'number' : '3002929609'
    },

    2 :{
        'name' : 'consuelo torres',
        'pay' : 350,
        'number' : '3168858481'
    },

    3 :{
        'name' : 'pedro perez',
        'pay' : 200,
        'number' : '3168'
    },

    4 :{
        'name' : 'pedro perez',
        'pay' : 150,
        'number' : '3168'
    },
}

while_exercise3(empleados)
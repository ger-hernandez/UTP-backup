
def estudioDemografico(poblacion:tuple, n:int):
    #checkeamos que los valores sean validos
    if(poblacion[0] >= poblacion [1]):
        return 'Los valores de las poblaciones no son adecuados para el estudio'
    #asignamos los valores de la tupla a dos variables
    pob_x = poblacion[0]
    pob_y = poblacion[1]

    d_salida = {}
    #con este loop vamos modificando el diccionario de salida
    #lo ejecutamos segun la cantidad de ciclos
    for i in range(1, n + 1):
        cant_anios = 0
        temp_pob_x = pob_x
        temp_pob_y = pob_y
        while(temp_pob_x < temp_pob_y):
            temp_pob_x += int(temp_pob_x * 0.08)
            temp_pob_y += int(temp_pob_y * 0.035)
            cant_anios += 1
        d_salida.update({f'anio{i}' : cant_anios, f'pobX{i}' : temp_pob_x, f'pobY{i}' : temp_pob_y})
        # d_salida[f'anio{i}'] = cant_anios
        # d_salida[f'PobX{i}'] = temp_pob_x
        # d_salida[f'PobY{i}'] = temp_pob_y
        #si la ejecucion ya se ejecuto las veces solicitadas salimos del loop
        # si no, incrementamos las poblaciones
        if not i == n:
            pob_x = int(poblacion[0] * 1.07 ** (i))
            pob_y = int(poblacion[1] * 1.18 ** (i))
    return d_salida

poblacion = (1000, 2000)
print(estudioDemografico(poblacion, 4))
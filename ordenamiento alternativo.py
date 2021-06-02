################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


from random import shuffle
from time import time


def ordenar(*args):
       
    """
    Ordena los números(args) de mayor a menor, mediante aleatoriedad,
    contando la cantidad de intentos y tiempo que demora en hacerlo.

    """       
                               
    if not all(type(x) in (int,float) for x in args):
        print ("Error, sólo números son válidos como argumentos")
        return                           #sale de la función si tiene argumentos que no sean números
        
    
    inicio = time()                      #cuenta el tiempo total que demora el programa en ordenar
    intentos = 0                         #cuenta la cantidad de intentos que hace el while
    
    
    l = list(args)                       #creo una lista donde guardo los argumentos para luego ordenarlos
    m = tuple(args)                      #creo una tupla inmutable con los argumentos originales
    indices = list(range(len(args)))     #creo una lista de índices que coincida con los argumentos

    condiciones = "l[0]"                 #cadena donde se agregarán las condiciones según el número de argumentos
    

    for i,num in enumerate(args):        #este bucle añade la cantidad de condiciones segun la cantidad de 'args'
        if i == 0:                       #omite el item cero, porque ya esta está incluido en 'condiciones'
            continue        
        
        condiciones += f">=l[{i}]"       #añade a la cadena 'condiciones' el índice de cada argumento ingresado


    while not eval(f"{condiciones}"):    #evalúa la cadena 'condiciones', y mientras NO estén ordenados:
            
        shuffle(indices)                 #ordena al azar la lista 'indices'
        
        for i in indices:
            l[indices[i]] = m[i]         #asigna un único índice de 'indices' a cada elemento de 'l'
        
        intentos = intentos + 1          #cuenta el intento del bucle
        
    print (f"{intentos} intentos en {round(time()-inicio,1)} segundos")
    return l
        



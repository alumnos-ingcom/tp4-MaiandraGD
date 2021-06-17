################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ11
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_palindromo(palabra, caps=False):

    """
    Evalúa si el texto ingresado es palíndromo
    El argumento Caps determina si se omite la distinción de mayusculas
    """
    
    
    if caps==True:      
        palabra = str(palabra).upper()
        return palabra == palabra[::-1]
    else:
        palabra = str(palabra)
        return palabra == palabra[::-1]
    

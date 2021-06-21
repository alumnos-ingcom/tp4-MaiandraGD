################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ7
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def division(a,b):

    """
    Esta funcion retorna (cociente,resto).
    Si el divisor es menor que el dividendo retorna False
    """
    
    if a<b:
        return False
    
    if b == 0:
        raise ZeroDivisionError
    
    cociente=0
    
    while a >= b:
        a = a-b
        resto = a
        cociente+=1
    
    return cociente,resto
    
    
if __name__ == "__main__":
    print(division(5,2))
    
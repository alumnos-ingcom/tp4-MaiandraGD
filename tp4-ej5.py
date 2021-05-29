################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ5
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def signo(numero):
    
    """
    Evalúa si un número es positivo, negativo o cero
    """    
    
    try:
        numero = int(numero)
        if numero > 0:
            print ("Positivo")
        elif numero < 0:
            print ("Negativo")
        else:
            print ("Cero")
            
    except ValueError:
        print("Eso no era un numero")
        
        
  
        
        

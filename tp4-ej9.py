################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ2
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_primo(numero):
    
    if abs(numero) == 0:
        primo = False
    else:
        primo = True
        
    for i in range(2, abs(numero)):                 
                  
        if abs(numero) % i == 0:            
            primo = False
            
    return primo    
        


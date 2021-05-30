################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ8
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def ordenar_mayor_a_menor(a, b, c):
          
    if a > b and a > c:        
        if b > c:
            orden = (a,b,c)
            return orden
        else:
            orden = (a,c,b)                        
            return orden
        
    if b > a and b > c:       
        if a > c:            
            orden = (b,a,c)
            return orden
        else:
            orden = (b,c,a)            
            return orden
        
    if c > a and c > b:
        if a > b:
            orden = (c,a,b)
            return orden
        else:
            orden = (c,b,a)
            return orden
    
    
def ordenar_menor_a_mayor(a, b, c):
    
     if a > b and a > c:        
        if b > c:
            orden = (c,b,a)
            return orden
        else:
            orden = (b,c,a)                        
            return orden
        
     if b > a and b > c:       
        if a > c:            
            orden = (c,a,b)
            return orden
        else:
            orden = (a,c,b)            
            return orden
        
     if c > a and c > b:
        if a > b:
            orden = (b,a,c)
            return orden
        else:
            orden = (a,b,c)
            return orden
    

# intentar realizarlo de forma dinámica con un bucle

    

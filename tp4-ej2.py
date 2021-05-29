################
# Giuliano Daniele - @MaiandraGD
# TP4-EJ2
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def suma_lenta():
    num1 = int(input("Ingrese el primero numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    while num2 > 0:
        num1 = num1 + 1
        num2 = num2 - 1
    print(num1)
    
if __name__ == "__main__":
    suma_lenta()


# no funciona si el segundo numero es negativo
# podría probar con valor absoluto o un condicional
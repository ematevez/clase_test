"""Consigna
Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

Información a tener en cuenta:

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""
def año_usuario():
    pregunta = int(input("Escoge el año que deseas corroborar: "))
    return pregunta

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def chequeo_año(año):
    if año <= 0:
        print("Elige un número correspondiente.")
    else: 
        if es_bisiesto(año):
            print("El año que escogiste es bisiesto.")
        else:
            print("El año que escogiste no es bisiesto.")

def main():
    pregunta = año_usuario()
    chequeo_año(pregunta)

main()

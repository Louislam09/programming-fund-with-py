from time import sleep
from os import system
import math


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)
    return number


def find_value():
    system('cls')
    print("""
********************************************************
PROGRAMA QUE ACEPTA EL VALOR DE A,B Y C Y MUESTA EL 1X Y
2X SEGUN LA FORMULA DE UNA ECUACION DE SEGUNDO GRADO
********************************************************
\n""")

    a_value = ask_number('Escriba el valor de A: ')
    b_value = ask_number('Escriba el valor de B: ')
    c_value = ask_number('Escriba el valor de C: ')

    d = b_value * -1
    e = math.sqrt((b_value * b_value) - (4 * a_value * c_value))
    f = 2 * a_value

    x1 = (d + e) / f
    x2 = (d - e) / f

    print(f"Este es el valor de x1: {x1}")
    print(f"Este es el valor de x2: {x2}")

    sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        find_value()
    else:
        print('\nGRACIAS POR UTILIZARME!')


find_value()

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


def find_hypotenuse():
    system('cls')
    print("""
*******************************************************
PROGRAMA QUE ACEPTA DOS CATETOS Y MUESTRA LA HIPOTENUSA
*******************************************************
\n""")

    ady_leg = ask_number('Escribe el valor del cateto adyancente: ')
    op_leg = ask_number('Escribe el valor del cateto opusto: ')

    hypotenuse = round(math.sqrt(ady_leg ** 2 + op_leg ** 2))

    print(f"\nLa Hipotenusa es: {hypotenuse}")

    sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        find_hypotenuse()
    else:
        print('\nGRACIAS POR UTILIZARME!')


find_hypotenuse()

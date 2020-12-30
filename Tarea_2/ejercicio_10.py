from time import sleep
from os import system
import math
import datetime


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)
    return number


def multi_number(num, multiplier):
    print(f"""\n
****************************************
TABLA DEL NUMERO {num} DEL 1 AL 13
****************************************
""")
    for i in range(13):
        multiplier = multiplier + 1
        print(f"{multiplier} X {num} = {multiplier*num}")


def start_multiply():
    system('cls')
    print("""
----------------------------------------------------------------
PROGRAMA QUE ACEPTA UN NUMERO Y CALCULA LA TABLA DE MULTIPLICAR
            DE DICHO NUMERO DEl 1 A HASTA EL 13
----------------------------------------------------------------
\n""")

    number_for_multiply = ask_number("Escribe el numero a multiplicar: ")

    for i in range(1):
        multi_number(number_for_multiply, i)

    sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        start_multiply()
    else:
        print('\nGRACIAS POR UTILIZARME!')


start_multiply()

import time
from os import system

global nombres_de_los_numeros


def ask_number(txt):

    try:
        global number

        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)

    return number


numbers_name = ['UNO',
                'DOS',
                "TRES",
                "CUATRO",
                "CINCO",
                "SEIS",
                "SIETE",
                "OCHO",
                "NUEVE",
                "DIEZ",
                "ONCE",
                "DOCE",
                "TRECE",
                "CATORCE",
                "QUINCE",
                "DIECISEIS",
                "DIECESIETE",
                "DIECIOCHO",
                "DIECINUEVE",
                "VEINTE"]


def print_number_name():
    system('cls')
    print("""
***************************************************
PROGRAMA QUE PIDE UN NUMERO Y LO MUESTRA EN LETRA
***************************************************
    \n""")

    given_number = ask_number('Escribe un numero del 1 al 20: ')

    if given_number <= 20:
        print("\nHaz Escrito el numero: " + numbers_name[given_number - 1])

        time.sleep(2)
        print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
        option = ask_number('RESPUESTA: ')

        if option == 1:
            print_number_name()
        else:
            print('\nGRACIAS POR UTILIZARME!')

    else:
        print(f"El numero {given_number} no esta entre los numeros del 1-20")
        time.sleep(2)
        system('cls')
        print_number_name()


print_number_name()

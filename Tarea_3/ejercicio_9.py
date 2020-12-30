import time
from os import system

global nombres_de_los_numeros

title = """
*******************************************************
PROGRAMA QUE PIDE UN NUMERO(1-30) Y LO MUESTRA EN LETRA
********************************************************
    \n"""


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
number_30 = "TRENTA"


def try_again():
    time.sleep(2)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        print_number_name()
    else:
        print('\nGRACIAS POR UTILIZARME!')


def print_number_name():
    system('cls')
    print(title)

    given_number = ask_number('Escribe un numero del 1 al 30: ')

    if given_number <= 20:
        print("\nHaz Escrito el numero: " + numbers_name[given_number - 1])
    elif given_number > 20 and given_number < 30:
        second_digit = str(given_number)[1]
        print("\nHaz Escrito el numero: " +
              numbers_name[19] + " y " + numbers_name[int(second_digit) - 1])
    elif given_number == 30:
        print("\nHaz Escrito el numero: " + number_30)

    else:
        print(f"El numero {given_number} no esta entre los numeros del 1-30")
        time.sleep(2)
        system('cls')
        print_number_name()

    try_again()


print_number_name()

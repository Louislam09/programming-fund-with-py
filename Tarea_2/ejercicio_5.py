import time
from os import system


def ask_number(txt):

    try:
        global number

        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)

    return number


global roman_numbers

roman_numbers = [
    " ",
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX"
]
_10_roman = "X"
_20_roman = "XX"
_30_roman = "XXX"
_40_roman = "XL"
_50_roman = "L"


def number_digit():
    system('cls')
    print("""
********************************************************
PROGRAMA QUE PIDE UN NUMERO(1-50) Y LO MUESTRA EN ROMANO
********************************************************
\n""")

    given_number = ask_number('Escribe un numero: ')
    given_number = str(given_number)

    if int(given_number) > 50:
        print("El numero dado es mayor a 50\nEscriba uno entre 1 y 50")
        time.sleep(3)
        number_digit()

    if len(given_number) == 1:
        print(f"\nEl numero {given_number} en romano es : " +
              roman_numbers[int(given_number)])

    if len(given_number) == 2 and int(given_number) <= 50:
        digit_one = given_number[0]
        digit_two = given_number[1]

        if digit_one == "1":
            print(f"\nEl numero {given_number} en romano es : " +
                  _10_roman + roman_numbers[int(digit_two)])
        elif digit_one == "2":
            print(f"\nEl numero {given_number} en romano es : " +
                  _20_roman+roman_numbers[int(digit_two)])
        elif digit_one == "3":
            print(f"\nEl numero {given_number} en romano es : " +
                  _30_roman+roman_numbers[int(digit_two)])
        elif digit_one == "4":
            print(f"\nEl numero {given_number} en romano es : " +
                  _40_roman+roman_numbers[int(digit_two)])
        else:
            print(f"\nEl numero {given_number} en romano es : " +
                  _50_roman)

    time.sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        number_digit()
    else:
        print('\nGRACIAS POR UTILIZARME!')


number_digit()

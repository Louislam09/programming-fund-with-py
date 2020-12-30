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


def find_age():
    system('cls')
    print("""
************************************************************
PROGRAMA QUE ACEPTA LA FECHA DE NACIMIENTO Y MUESTRE LA EDAD
*************************************************************
\n""")

    date = datetime.datetime.now()
    get_day = date.day
    get_month = date.month
    get_year = date.year

    day = ask_number('Escribe tu dia de naciento: ')
    month = ask_number('Escribe tu mes de naciento: ')
    year = ask_number('Escribe el año de tu naciento: ')

    if year > get_year or day > 31 or month > 12:
        print(f'\nEs imposible que naciera el {day}/{month}/{year}')
        sleep(2)
        return find_age()
    if year == get_year and month > get_month:
        print(f'\nEs imposible que naciera el {day}/{month}/{year}')
        sleep(2)
        return find_age()
    if year == get_year and day > get_day:
        print(f'\nEs imposible que naciera el {day}/{month}/{year}')
        sleep(2)
        return find_age()

    age = get_year - year

    if month == get_month and day <= get_day and age >= 1:
        age = age
        print(f"Tu edad es: {age} años")

    elif month == get_month and day > get_day and age >= 1:
        age = age - 1
        print(f"Tu edad es: {age} años")

    elif month > get_month and age >= 1:
        age = age - 1
        print(f"Tu edad es: {age} años")

    elif month < get_month and age >= 1:
        age = age
        print(f"Tu edad es: {age} años")

    elif month < get_month and age == 0:
        age = get_month - month
        print(f"Tu edad es: {age} Mes/Meses")
    elif month == get_month and day <= get_day and age == 0:
        age = get_day - day
        print(f"Tu edad es: {age} dia/s")

    sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        find_age()
    else:
        print('\nGRACIAS POR UTILIZARME!')


find_age()

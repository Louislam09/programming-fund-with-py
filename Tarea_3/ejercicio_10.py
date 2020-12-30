from os import system
from math import floor

title = """
*******************************************************
PROGRAMA QUE TE DIGA CUANDO BOLETOS DE LA GUAGUA DEL 
    ITLA PUEDES COMPRAR CON X CANTIDAD DE DINERO
********************************************************
\n"""

ticket_price = 25


def ask_number(txt):
    try:
        global number

        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)

    return number


def try_again():
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        count_ticket_by_money()
    else:
        print('\nGRACIAS POR UTILIZARME!')


def count_ticket_by_money():
    system("cls")
    print(title)
    amount_of_money = ask_number("Escriba la cantidad de dinero: ")
    if amount_of_money % ticket_price == 0:
        tickets = floor(amount_of_money / ticket_price)
        print("\n Con {} pesos. Puedes comprar {} ticket(s)".format(
            amount_of_money, tickets))
    else:
        tickets = floor(amount_of_money / ticket_price)
        residuo = amount_of_money % ticket_price
        print("\n Con {} pesos. Puedes comprar {} ticket(s) y te queda {} pesos.".format(
            amount_of_money, tickets, residuo))

    try_again()


count_ticket_by_money()

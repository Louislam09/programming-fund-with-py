from os import system

title = """
*******************************************************
    PROGRAMA QUE ACEPTE UN NUMERO E IDIQUE SI ES PAR
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


def try_again():
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = ask_number('RESPUESTA: ')

    if option == 1:
        is_evet()
    else:
        print('\nGRACIAS POR UTILIZARME!')


def is_evet():
    system('cls')
    print(title)

    number = ask_number("Escribe un numero: ")

    if number % 2 == 0:
        print("Este numero es: Par")
    else:
        print("Este numero es: Impar")

    try_again()


is_evet()

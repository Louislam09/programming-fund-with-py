from os import system

title = """
*******************************************************
    PROGRAMA QUE ACEPTE 3 NUMEROS E INDIQUE CUAL ES EL 
            MAYOR Y EL MENOR DE LOS MISMOS
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
        who_higher_and_lower()
    else:
        print('\nGRACIAS POR UTILIZARME!')


def who_higher_and_lower():
    system('cls')
    print(title)
    number_1 = ask_number('Escribe el primer numero: ')
    number_2 = ask_number('Escribe el segundo numero: ')
    number_3 = ask_number('Escribe el tercer numero: ')

    numbers = [number_1, number_2, number_3]

    numbers.sort()

    print(f"""
De los tres el mayor es:  {numbers[2]}  
y el menor es:  {numbers[0]} 
    """)


who_higher_and_lower()

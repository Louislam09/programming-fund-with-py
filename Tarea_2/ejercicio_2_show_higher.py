from os import system
system('cls')

print("""
***************************************************
PROGRAMA QUE PIDA TRES NUMEROS Y MUESTRE EL MAYOR
***************************************************
\n""")

global numeros
numeros = []


def ask_number(txt):

    try:
        global nota

        nota = input(txt)
        nota = int(nota)
        numeros.append(nota)
    except:
        print(f">>>{nota}" + " no es un numero\n")
        ask_number(txt)

    return nota


def start_program():
    ask_number("Escriba el primer numero: ")
    ask_number("Escriba el segundo numero: ")
    ask_number("Escriba el tercer numero: ")

    numeros.sort(reverse=True)

    print("\nEl numero mayor es: " + str(numeros[0]))


start_program()

print('\nGracias por utilizarme!')
input()

from os import system
system('cls')

print("""
***************************************************
PROGRAMA QUE PIDA 4 NOTA Y CALCULA EL PROMEDIO
***************************************************
\n""")


def ask_nota(txt):

    try:
        global nota
        nota = input(txt)
        nota = int(nota)
    except:
        print(f">>>{nota}" + " no es un numero\n")
        ask_nota(txt)

    return nota


nota_1 = ask_nota('Escribe la primera nota: ')
nota_2 = ask_nota('Escribe la segunda nota: ')
nota_3 = ask_nota('Escribe la tercera nota: ')
nota_4 = ask_nota('Escribe la cuarta nota: ')

suma_de_nota = nota_1 + nota_2 + nota_3 + nota_4
system('cls')

promedio = suma_de_nota / 4

print("\nEl Promedio Es : " + str(promedio) + "\n")

input('\nPresione cualquier tecla para salir...')

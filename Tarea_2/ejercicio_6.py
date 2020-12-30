from time import sleep
from os import system


def reverse_word():
    system('cls')
    print("""
********************************************
PROGRAMA QUE PIDE UNA PALABRA Y LA INVIERTE
********************************************
\n""")
    word = input('Escribe una palabra: ')

    new_word = list(word)
    new_word.reverse()

    reversed_word = "".join(new_word)

    words = f"""\n
    Original: {word}
    Invertida: {reversed_word}
    """
    print(words)

    sleep(1)
    print('\nQUIERES PROBAR DE NUEVOO ? \n 1) SI \n 2) NO')
    option = input('RESPUESTA: ')

    if option == "1":
        reverse_word()
    else:
        print('\nGRACIAS POR UTILIZARME!')


reverse_word()

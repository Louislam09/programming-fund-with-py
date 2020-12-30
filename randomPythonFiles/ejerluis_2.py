def leer_palabra():
    global word
    word = input("Inserte una palabra: ")


def contar_letra():
    contador = 0
    for i in word:
        if i.isalpha():
            contador += 1

    print("La cantidad de letras es ", contador, "!")


leer_palabra()
contar_letra()
input("Presiona una tecla para terminar")

# word = input('Inserte un palabra: ')
# num = list(word)
# print(len(num))
# input('Presiona una tecla para terminar')


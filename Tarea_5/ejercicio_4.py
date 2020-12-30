# ---------------------------------------------
# PROGRAMA QUE ACEPTA UNA FRASE APROBADO POR LA
# RAE Y LA MUESTRE EN ESPAGNOL
# ---------------------------------------------

from textblob import TextBlob
from os import system


title = """
---------------------------------------------
PROGRAMA QUE ACEPTA UNA FRASE APROBADO POR LA
     RAE Y LA MUESTRE EN ESPAGNOL
---------------------------------------------
"""


def translate_phrase():
    system('cls')
    print(title)

    try:

        phrase = input("Escribe la frase a traduccir: ")
        while len(phrase) < 1:
            phrase = input("Escribe la frase a traduccir: ")

        to_traslate = TextBlob(phrase)
        translated_phrase = to_traslate.translate(to="en")

        print("""
      ---------------
    * FRASE TRADUCIDA *
      ---------------
      """)

        print(f"|>>>| {translated_phrase} |<<<|")

        print("\nQuieres traduccir otra frase?")
        option = input("\n1) Si \n2) No y terminar.\n-opcion: ")
        if option == "1":
            translate_phrase()
        else:
            system("exit")

    except:
        print(f"""\n
    ---------------------------------------------
            NO TIENES CONEXION A INTERNET!
            COMPRUEBA TU CONEXION E INTENTA
            DE NUEVO!
    ---------------------------------------------
        """)


translate_phrase()

print("\nPresiona  cualquier tecla para salir....")
input()

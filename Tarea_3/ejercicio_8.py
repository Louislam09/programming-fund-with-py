import os

print("""
*****************************************************************
      PROGRAMA QUE ACEPTE UN DIA Y MES DE CUMPLEÑOS DE UNA
    PERSONA Y MUESTRE EL SIGNO DEL ZODIACO QUE LE CORRESPONDE 
*****************************************************************
\n""")


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)
    return number


dia = ask_number('Escribe tu dia de nacimiento: ')
mes = ask_number('Escribe tu mes de nacimiento(1-12): ')

print("\n")


def get_zodiac(dia, mes):
    if dia > 31 or dia <= 0 or mes > 12 or mes <= 0:
        print("No tienes signo de zodiaco porque no eres de este planeta! X'D")
        return
    if (dia >= 21 and mes == 3 or dia <= 20 and mes == 4):
        print("Tu signo del zodiaco es: Aries")
    elif (dia >= 21 and mes == 4 or dia <= 21 and mes == 5):
        print("Tu signo del zodiaco es: Tauro")
    elif (dia >= 22 and mes == 5 or dia <= 21 and mes == 6):
        print("Tu signo del zodiaco es: Géminis")
    elif (dia >= 22 and mes == 6 or dia <= 22 and mes == 7):
        print("Tu signo del zodiaco es: Cáncer")
    elif (dia >= 23 and mes == 7 or dia <= 23 and mes == 8):
        print("Tu signo del zodiaco es: Leo")
    elif (dia >= 24 and mes == 8 or dia <= 23 and mes == 9):
        print("Tu signo del zodiaco es: Virgo")
    elif (dia >= 24 and mes == 9 or dia <= 23 and mes == 10):
        print("Tu signo del zodiaco es: Libra")
    elif (dia >= 24 and mes == 10 or dia <= 22 and mes == 11):
        print("Tu signo del zodiaco es: Escorpio")
    elif (dia >= 23 and mes == 11 or dia <= 21 and mes == 12):
        print("Tu signo del zodiaco es: Sagitario")
    elif (dia >= 22 and mes == 12 or dia <= 20 and mes == 1):
        print("Tu signo del zodiaco es: Capricornio")
    elif (dia >= 21 and mes == 1 or dia <= 18 and mes == 2):
        print("Tu signo del zodiaco es: Acuario")
    elif (dia >= 19 and mes == 2 or dia <= 20 and mes == 3):
        print("Tu signo del zodiaco es: Piscis")


get_zodiac(dia, mes)

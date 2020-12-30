
import os

print("""
***************************************************
PROGRAMA QUE ACEPTE UNA CALIFICACION Y MUESTRE EL 
        EQUIVALENTE LITERAL (A,B,C o F)
***************************************************
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


qualification = ask_number('Escribe una calificacion: ')


def rank_qualification(number):
    if number >= 90 and number <= 100:
        print("Su calificacion es una: A")
    elif number >= 80 and number <= 89:
        print("Su calificacion es una: B")
    elif number >= 70 and number <= 79:
        print("Su calificacion es una: C")
    else:
        print("Su calificacion es una: F")


rank_qualification(qualification)

# 100-90 = A (EXCELENTE)
# 89-80 = B (MUY BUEN0)
# 79-70 = C (BUENO)
# 69-60 = D (POCO SASTIFACTORIO)
# 0-59 = F (MALA)

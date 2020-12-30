import math
from os import system
from time import sleep

timer = 0

title_1 = """ 
 _________________________________________________________________
*                                                                 *
*                                                                 *   
*        █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█ ▄▀█                        *
*        █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ █▀█                        *
*                                                                 *
*                                                                 *
*                                                                 *
*                                                                 *
*                                                                 *
*_________________________________________________________________*
"""
title_2 = """ 
 _________________________________________________________________
*                                                                 *
*                                                                 *   
*        █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█ ▄▀█   █▀█ ▄▀█ █▀█ ▄▀█      *
*        █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ █▀█   █▀▀ █▀█ █▀▄ █▀█      *
*                                                                 *
*                                                                 *
*                                                                 *
*                                                                 *
*                                                                 *
*_________________________________________________________________*
"""
title_3 = """ 
 _________________________________________________________________
*                                                                 *
*                                                                 *   
*        █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█ ▄▀█   █▀█ ▄▀█ █▀█ ▄▀█      *
*        █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ █▀█   █▀▀ █▀█ █▀▄ █▀█      *
*                                                                 *
*    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀█                              *
*    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▀▄                              *
*                                                                 *
*                                                                 *
*_________________________________________________________________*
"""
title_4 = """ 
 _________________________________________________________________
*                                                                 *
*                                                                 *   
*        █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█ ▄▀█   █▀█ ▄▀█ █▀█ ▄▀█      *
*        █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ █▀█   █▀▀ █▀█ █▀▄ █▀█      *
*                                                                 *
*    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀█   █▀▀ █░░                    *
*    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▀▄   ██▄ █▄▄                    *
*                                                                 *
*                                                                 *
*_________________________________________________________________*
"""
title_5 = """ 
 ___________________________________________________________________
*                                                                   *
*                                                                   *   
*        █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█ ▄▀█   █▀█ ▄▀█ █▀█ ▄▀█        *
*        █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ █▀█   █▀▀ █▀█ █▀▄ █▀█        *
*                                                                   *
*    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀█   █▀▀ █░░   ▄▀█ █▀█ █▀▀ ▄▀█    *
*    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▀▄   ██▄ █▄▄   █▀█ █▀▄ ██▄ █▀█    *
*                                                                   *
*                                                                   *
*__________________________________________________________________ *
"""

final_massage = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░╔═════════════════════════════════════╗░░░░
░░║░╔═══╗╔═══╗╔═══╗╔═══╗╔══╗╔═══╗╔═══╗░░║░░░░
░░║░║╔═╗║║╔═╗║║╔═╗║║╔═╗║╚╣╠╝║╔═╗║║╔═╗║░░║░░░░
░░║░║║░╚╝║╚═╝║║║░║║║║░╚╝░║║░║║░║║║╚══╗░░║░░░░
░░║░║║╔═╗║╔╗╔╝║╚═╝║║║░╔╗░║║░║╚═╝║╚══╗║░░║░░░░
░░║░║╚╩═║║║║╚╗║╔═╗║║╚═╝║╔╣╠╗║╔═╗║║╚═╝║░░║░░░░
░░║░╚═══╝╚╝╚═╝╚╝░╚╝╚═══╝╚══╝╚╝░╚╝╚═══╝░░║░░░░
░░║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░╔═══╗╔═══╗╔═══╗░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░║╔═╗║║╔═╗║║╔═╗║░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░║╚═╝║║║░║║║╚═╝║░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░║╔══╝║║░║║║╔╗╔╝░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░║║░░░║╚═╝║║║║╚╗░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░╚╝░░░╚═══╝╚╝╚═╝░░░░░░░░░░░║░░░░
░╔╗░╔╦════╦══╦╗░░╔══╦════╦═══╦═══╦═╗╔═╦═══╗░░
░║║░║║╔╗╔╗╠╣╠╣║░░╚╣╠╩══╗═║╔═╗║╔═╗║║╚╝║║╔══╝░░
░║║░║╠╝║║╚╝║║║║░░░║║░░╔╝╔╣║░║║╚═╝║╔╗╔╗║╚══╗░░
░║║░║║░║║░░║║║║░╔╗║║░╔╝╔╝║╚═╝║╔╗╔╣║║║║║╔══╝░░
░║╚═╝║░║║░╔╣╠╣╚═╝╠╣╠╦╝═╚═╣╔═╗║║║╚╣║║║║║╚══╗░░
░╚═══╝░╚╝░╚══╩═══╩══╩════╩╝░╚╩╝╚═╩╝╚╝╚╩═══╝░░
░░║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║░░░░
░░║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║░░░░
░░╚═════════════════════════════════════╝░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
# final_massage = """
# ▒▒▒▒▒▒▐███████▌
# ▒▒▒▒▒▒▐░▀░▀░▀░▌
# ▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌
# ▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
# ▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐
# """


animate_text = [title_1, title_2, title_3, title_4, title_5]
new_char = ""


def animate_title(time):
    for title in animate_text:
        sleep(time)
        system('cls')
        print(title)
        new_char


def try_again():
    print("\nQuieres probar de nuevo ? \n1) SI\n2) NO")
    option = input('\nRespuesta: ')
    if option == "1":
        global timer
        timer = 0
        calculate_the_area()
    else:
        # return print('\nGracias por utilizarme !!')
        system('cls')
        print(final_massage)


def ask_number(txt):

    try:
        global number

        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)

    return number


def calculate_the_area():
    system('cls')
    animate_title(timer)
    base = ask_number("Escriba el valor de la base: ")
    altura = ask_number("Escriba el valor de la altura: ")

    area = (base * altura) / 2

    print('El area del triangulo es: %s' % area)

    try_again()


calculate_the_area()
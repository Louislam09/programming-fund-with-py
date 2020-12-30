# Nombre: Luis Alejandro Martinez
# Matricula: 20197725

import os
import pandas as pd
import time
import webbrowser as wb

DIARY_MEMORY = []
link_url = 'https://youtu.be/gyYtxGrZRG0'

TITLE = "MY AGENDA"


def ask_data(txt):
    global content
    content = input(txt)

    if len(content) == 0:
        ask_data(txt)

    return content


def save_diary_memory(person):
    DIARY_MEMORY.append(person)
    dataFrame = pd.DataFrame(DIARY_MEMORY, columns=[
                             'Nombre', 'Apellido', 'Telefono', 'Email', 'FechaDeNacimiento', 'UsuarioInstagram', 'Comentario'])
    dataFrame.to_csv("DIARY_STORAGE.csv")


def get_diary_memory():
    if os.path.isfile("DIARY_STORAGE.csv"):
        DIARY_STORAGED = pd.read_csv("DIARY_STORAGE.csv").values.tolist()

        for i in range(len(DIARY_STORAGED)):
            DIARY_STORAGED[i].remove(i)
        for person in DIARY_STORAGED:
            DIARY_MEMORY.append(person)


class Diary:
    def __init__(self, onwer):
        self.onwer = onwer
        self.contacts = DIARY_MEMORY

    def add_person(self):
        os.system('cls')
        print("SECTION PARA ANADIR CONTACTO\n")
        save_diary_memory(Person().ask_info())

        print('Presione cualquier tecla para volver al Menu...')
        input()
        Menu()

    def modify_person(self):

        os.system('cls')
        print("SECTION PARA MODIFICAR CONTACTO \n")

        if len(DIARY_MEMORY) == 0:
            print("No hay contacto para modificar!")
            time.sleep(2)
            Menu()
        else:
            print("Elige el numero del contacto que quierEs modificar\n")

            for i in range(len(DIARY_MEMORY)):
                print(f"{i}- {DIARY_MEMORY[i][0]} {DIARY_MEMORY[i][1]}")

            index_of_person = int(input('Tu Eleccion: '))

            print("\nElije el numero del dato que quieres modificar de este contacto\n")

            print("""
            1-Nombre
            2-Apellido
            3-Telefono
            4-Email
            5-fecha de nacimeinto
            6-usuario de instagram
            7-comentario
            """)

            index_of_data = int(input("Tu eleccion es: "))

            if index_of_data == "5":
                day = ask_data('Escribe el nuevo dia de nacimiento: ')
                month = ask_data('Escribe el nuevo mes de nacimiento: ')
                year = ask_data('Escribe el nuevo año de nacimiento: ')
                new_data = f"{day}-{month}-{year}"
            else:
                new_data = ask_data('Escribe el numero dato: ')

            index_of_data = index_of_data - 1

            DIARY_MEMORY[index_of_person][index_of_data] = new_data

            dataFrame = pd.DataFrame(DIARY_MEMORY, columns=[
                                     'Nombre', 'Apellido', 'Telefono', 'Email', 'FechaDeNacimiento', 'UsuarioInstagram', 'Comentario'])
            dataFrame.to_csv("DIARY_STORAGE.csv")
            print('Persona persona modificada con exito!\n')

            print('Presione cualquier tecla para volver al Menu...')
            input()
            Menu()

    def delete_person(self):
        os.system('cls')
        print("SECTION PARA ELIMINAR CONTACTO \n")

        if len(DIARY_MEMORY) == 0:
            print("No hay contacto para eliminar!")
            time.sleep(2)
            Menu()
        else:
            print("Elige el numero del contacto que quieras eliminar\n")

            for i in range(len(DIARY_MEMORY)):
                print(f"{i}- {DIARY_MEMORY[i][0]} {DIARY_MEMORY[i][1]}")

            index_of_person = int(input('Tu Eleccion: '))

            DIARY_MEMORY.remove(DIARY_MEMORY[index_of_person])

            dataFrame = pd.DataFrame(DIARY_MEMORY, columns=[
                                     'Nombre', 'Apellido', 'Telefono', 'Email', 'FechaDeNacimiento', 'UsuarioInstagram', 'Comentario'])
            dataFrame.to_csv("DIARY_STORAGE.csv")

            print('Persona eliminada con exito!\n')

            print('Presione cualquier tecla para volver al Menu...')
            input()
            Menu()

    def show_person(self):
        os.system('cls')
        print("Lista de Contactos \n")

        if len(DIARY_MEMORY) == 0:
            print("No hay contacto para eliminar!")
            time.sleep(2)
            Menu()
        else:
            for i in range(len(DIARY_MEMORY)):
                print(f"{i}- {DIARY_MEMORY[i][0]} {DIARY_MEMORY[i][1]}")

            print('Presione cualquier tecla para volver al Menu...')
            input()
            Menu()


my_diary = Diary('Luis')


class Person:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.phone_number = ""
        self.email = ""
        self.born_day = ""
        self.born_month = ""
        self.born_year = ""
        self.instagram_user = ""
        self.comment = ""
        self.born_date = ""

    def ask_info(self):
        self.name = ask_data('Escribe el nombre: ')
        self.last_name = ask_data('Escribe el apellido: ')
        self.phone_number = ask_data('Escribe el numero de telefono: ')
        self.email = ask_data('Escribe el email: ')
        self.born_day = ask_data('Escribe el dia de nacimiento: ')
        self.born_month = ask_data('Escribe el mes de nacimiento: ')
        self.born_year = ask_data('Escribe el año: ')
        self.instagram_user = ask_data('Escribe el usuario de instagram: ')
        self.comment = ask_data('Escribe un comentario: ')
        self.born_date = f"{self.born_day}-{self.born_month}-{self.born_year}"

        return [self.name, self.last_name, self.phone_number, self.email, self.born_date, self.instagram_user, self.comment]


def Menu():
    os.system('cls')
    print(TITLE)

    print("""
    1-Añadir Contacto
    2-Modificar Contacto
    3-Eliminar Contacto
    4-Mostrar Contacto
    5-Ver video en youtube
    6-Salir
    """)

    option = ask_data("Escribe tu opcion: ")

    if option == "1":
        my_diary.add_person()
    elif option == "2":
        my_diary.modify_person()
    elif option == "3":
        my_diary.delete_person()
    elif option == "4":
        my_diary.show_person()
    elif option == "5":
        wb.open(link_url)
    elif option == "6":
        print('Gracias por Utilizar nuestros servicios!')
    else:
        print(f"{option} no es una opcion")
        time.sleep(2)
        Menu()


get_diary_memory()
Menu()


# Nombre: Luis Alejandro Martinez
# Matricula: 20197725

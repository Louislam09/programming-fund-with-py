# Nombre: Luis Alejandro Martinez
# Matricula: 2019-7725

import os
import pandas as pd
from time import sleep

TITLE = "Agenda\n"
DIARY_MEMORY = []


def ask_data(txt):
    try:
        global content
        content = input(txt)
        if len(content) == 0:
            ask_data(txt)
    except:
        print(f">>>{content}" + " no es valido; Intente de nuevo!\n")
        ask_data(txt)

    return content


def save_to_csv(name, last_name, phone_number, email, born_date, instagram_profile, comment):
    DIARY_MEMORY.append([name, last_name, phone_number,
                         email, born_date, instagram_profile, comment])

    dataFrame = pd.DataFrame(DIARY_MEMORY, columns=[
                             "Name", "Last_name", "Phone_number", "Email", "Born_date", "Social_media", "Commet"])
    dataFrame.to_csv("DIARY_MEMORY.csv")


def get_from_csv():
    if os.path.isfile("DIARY_MEMORY.csv"):
        DIARY_STORAGED = pd.read_csv("DIARY_MEMORY.csv").values.tolist()
        for i in range(len(DIARY_STORAGED)):
            DIARY_STORAGED[i].remove(i)
        for person in DIARY_STORAGED:
            DIARY_MEMORY.append(person)


class Diary:
    def __init__(self, owner):
        self.owner = owner
        self.contacts = DIARY_MEMORY

    def add_person(self, person):
        print("\nContacto agregado con exito!")

        print("\n Presione cualquier tecla para volver al menu...")
        input()
        Menu()

    def delete_person(self):
        os.system('cls')
        print("SECTION PARA ELIMINAR CONTACTO\n\n")

        if len(self.contacts) == 0:
            print("No hay contacto")
            sleep(2)
            Menu()
        else:
            for person in range(len(self.contacts)):
                print(
                    f"{person}- {self.contacts[person][0]} {self.contacts[person][1]}\n")

            index_of_person = int(input(
                'Escribe el numero del contacto que quieres elimirar: '))

            if index_of_person > len(self.contacts)-1:
                print(
                    f"Elija un numero del listado porque este no existe {index_of_person}\n")
                index_of_person = int(input(
                    'Escribe el numero del contacto que quieres elimirar: '))

            del (self.contacts[index_of_person])

            dataFrame = pd.DataFrame(self.contacts, columns=[
                "Name", "Last_name", "Phone_number", "Email", "Born_date", "Social_media", "Commet"])

            dataFrame.to_csv("DIARY_MEMORY.csv")

            print('\nContacto Elimido con exito!')

            print("\n Presione cualquier tecla para volver al menu...")
            input()
            Menu()

    def modify_person(self):
        os.system('cls')
        print("SECTION PARA MODIFICAR CONTACTO\n\n")

        if len(self.contacts) == 0:
            print("No hay contacto")
            sleep(2)
            Menu()
        else:
            for person in range(len(self.contacts)):
                print(
                    f"{person}- {self.contacts[person][0]} {self.contacts[person][1]}\n")

            try:
                index_of_person = int(input(
                    'Escribe el numero del contacto que quieres modificar: '))
            except:
                print("Las letras no son permitida; Digite un numero!")
                index_of_person = int(input(
                    'Escribe el numero del contacto que quieres modificar: '))

            if index_of_person > len(self.contacts)-1:
                print(
                    f"Elija un numero del listado porque este no existe {index_of_person}\n")
                index_of_person = int(input(
                    'Escribe el numero del contacto que quieres modificar: '))

            print("""\n
            Que dato quires modificar?

            1-Nombre
            2-Apellido
            3-Numero Telefonico
            4-Email
            5-Fecha de nacimineto
            6-usurario de Instagram
            7-Comentario
            """)

            try:
                index_of_data = int(input("Escriba el Numero del dato: "))

            except:
                print("Las letras no son permitida; Digite un numero!")
                index_of_data = int(input("Escriba el Numero del dato: "))

            if index_of_data > len(self.contacts[index_of_person]):
                index_of_data = int(input("Que dato quires modificar?: "))

            if index_of_data == 5:
                born_day = ask_data("Escribe el dia de nacimineto: ")
                born_month = ask_data("Escribe el mes de nacimineto: ")
                born_year = ask_data("Escribe el año de nacimineto: ")

                new_data = f"{born_day}-{born_month}-{born_year}"
            else:
                new_data = ask_data("Escribe el numero dato: ")

            index_of_data = index_of_data - 1

            self.contacts[index_of_person][index_of_data] = new_data

            dataFrame = pd.DataFrame(self.contacts, columns=[
                "Name", "Last_name", "Phone_number", "Email", "Born_date", "Social_media", "Commet"])

            dataFrame.to_csv("DIARY_MEMORY.csv")

            print('\nContacto modificado con exito!')

            print("\n Presione cualquier tecla para volver al menu...")
            input()
            Menu()

    def show_contacts(self):
        os.system('cls')
        print("LISTADO DE CONTACTO\n\n")

        if len(self.contacts) == 0:
            print("No hay contacto")
            sleep(2)
            Menu()
        else:
            for person in range(len(self.contacts)):
                # here I take from the storaged data the name and last_name of the person
                info = f"{self.contacts[person][0]} {self.contacts[person][1]}"
                print(f"{person}- {info}")

            print("\n Presione cualquier tecla para volver al menu...")
            input()
            Menu()


class Person:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.phone_number = ""
        self.email = ""
        self.born_day = ""
        self.born_month = ""
        self.born_year = ""
        self.instagram_profile = ""
        self.comment = ""
        self.born_date = ""

    def ask_person_info(self):
        os.system('cls')
        print("SECTION PARA AGREGAR CONTACTO\n\n")

        self.name = ask_data("Escribe el nombre: ")
        self.last_name = ask_data("Escribe el apellido: ")
        self.phone_number = ask_data("Escribe el numero de telefono: ")
        self.email = ask_data("Escribe el correo: ")
        self.born_day = ask_data("Escribe el dia de nacimineto: ")
        self.born_month = ask_data("Escribe el mes de nacimineto: ")
        self.born_year = ask_data("Escribe el año de nacimineto: ")
        self.instagram_profile = ask_data("Escribe tu usuario de Instagram: ")
        self.comment = ask_data("Escribe Un Comentario: ")
        self.born_date = f"{self.born_day}-{self.born_month}-{self.born_year}"

        save_to_csv(self.name, self.last_name, self.phone_number,
                    self.email, self.born_date, self.instagram_profile, self.comment)

        return [self.name, self.last_name, self.phone_number, self.email, self.born_date, self.instagram_profile, self.comment]


my_diary = Diary("Luis")


def Menu():
    os.system('cls')
    print(TITLE)

    print("""
    1.Agregar Contacto 
    2.Modificar Contacto
    3.Eliminar Contacto
    4.Mostrar Contacto
    5.Salir
    """)
    try:
        option = int(ask_data("Escribe Tu Opcion: "))
    except:
        print("Las letras no son permitida; Digite un numero!")
        option = int(ask_data("Escribe Tu Opcion: "))

    while option > 5:
        print(f"El {option} No Es Una Opcion; Elige Una Opcion!")
        option = int(ask_data("Escribe Tu Opcion: "))

    if option == 1:
        my_diary.add_person(Person().ask_person_info())

    elif option == 2:
        my_diary.modify_person()

    elif option == 3:
        my_diary.delete_person()

    elif option == 4:
        my_diary.show_contacts()
    elif option == 5:
        return


get_from_csv()
Menu()

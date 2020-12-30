# Nombre: Luis Alejandro Martinez
# Matricula: 2019-7725

from os import system
from time import sleep
import pandas as pd
import webbrowser as wb
import os
import folium
import playsound


TITLE = "Programa para registrar datos de personas desaparecidas\n"
SPACE = "    "


data = []
tags = []
li_tag = []
li_tag_with_zodiac = []

# explosionSound = 'explosion.wav'
# FUNCTION SOUNDS
menu_sound = "function_sound/menu_sound.m4a"
file_generate_sound = "function_sound/file_generate_sound.m4a"
map_generate_sound = "function_sound/map_generate_sound.m4a"
invalid_option_sound = "function_sound/invalid_option_sound.m4a"
list_zodiac_sound = "function_sound/list_zodiac_sound.m4a"
not_data_sound = "function_sound/not_data_sound.m4a"
# ADD SOUNDS
born_day_sound = "add_missing_person_sounds/born_day_sound.m4a"
born_month_sound = "add_missing_person_sounds/born_month_sound.m4a"
born_year_sound = "add_missing_person_sounds/born_year_sound.m4a"
id_sound = "add_missing_person_sounds/id_sound.m4a"
write_name_sound = "add_missing_person_sounds/write_name_sound.m4a"
write_last_name_sound = "add_missing_person_sounds/write_last_name_sound.m4a"
write_gender_sound = "add_missing_person_sounds/write_gender_sound.m4a"
last_place_sound = "add_missing_person_sounds/last_place_sound.m4a"
latitude_sound = "add_missing_person_sounds/latitude_sound.m4a"
longitude_sound = "add_missing_person_sounds/longitude_sound.m4a"
another_info_sound = "add_missing_person_sounds/another_info_sound.m4a"
adding_last_sound = "add_missing_person_sounds/adding_last_sound.m4a"
# MODIFY SOUNDS
data_to_modify_sound = "modify_missing_person_sounds/data_to_modify_sound.m4a"
modifying_last_sound = "modify_missing_person_sounds/modifying_last_sound.m4a"
person_chosen_to_modify_sound = "modify_missing_person_sounds/person_chosen_to_modify_sound.m4a"
write_new_data_sound = "modify_missing_person_sounds/write_new_data_sound.m4a"


def ask_data(txt):
    try:
        global content
        content = input(txt)
        if len(content) == 0:
            ask_data(txt)
    except:
        print(f">>>{content}" + " no es valido; Intente de nuevo!\n")
        play_sound(invalid_option_sound)
        ask_data(txt)

    return content


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es una  opcione validad; Elija Una!\n")
        play_sound(invalid_option_sound)
        ask_number(txt)

    return number


def play_sound(sound_file):
    playsound.playsound(sound_file, True)


def is_adult(age):
    age = int((age.split("/")[2]))

    if 2020 - age > 17:
        return True
    else:
        return False


def save_to_csv(date, id, name,  last_name, gender, last_place, latitude, longitude, other_information, zodiac_sign):
    data.append([date, id, name,  last_name, gender, last_place,
                 latitude, longitude, other_information, zodiac_sign])

    dataFrame = pd.DataFrame(data, columns=[
                             "Fecha", "Cedula", "Nombre", "Apellidos", "Genero", "UltimoLugar", "Latitud", "Longitud", "Otra informacion", "Zodiaco"])
    dataFrame.to_csv("missing_people_db.csv")


def get_from_csv():
    if os.path.isfile("missing_people_db.csv"):
        storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
        for i in range(len(storaged_data)):
            storaged_data[i].remove(i)
        for person in storaged_data:
            data.append(person)


def add_missing_person():
    system('cls')
    print("Le Solicitare Algunos Datos Del Desaparecido\n")
    play_sound(born_day_sound)
    born_day = ask_number("Digite Su Dia de nacimineto : ")
    play_sound(born_month_sound)
    born_month = ask_number("Digite Su mes de nacimineto : ")
    play_sound(born_year_sound)
    born_year = ask_number("Digite Su año de nacimineto : ")

    born_date = f"{born_day}/{born_month}/{born_year}"

    zodiac_sign = get_zodiac(born_day, born_month)
    adult = is_adult(born_date)

    if adult:
        play_sound(id_sound)
        id = ask_data("Digita Su Cedula: ")
    else:
        id = "No Posee"

    play_sound(write_name_sound)
    name = ask_data("Escribe Su Nombre: ")
    play_sound(write_last_name_sound)
    last_name = ask_data("Escribe Su Apellido: ")
    play_sound(write_gender_sound)
    gender = ask_data("Escribe Su Genero(M/F): ")
    play_sound(last_place_sound)
    last_place = ask_data("Escribe El Ultimo Lugar Donde Fue Visto: ")
    play_sound(latitude_sound)
    latitude = ask_data("Digita La latitud: ")
    play_sound(longitude_sound)
    longitude = ask_data("Digita La longitud: ")
    play_sound(another_info_sound)
    other_information = ask_data("Otra informacion: ")

    save_to_csv(born_date, id, name, last_name, gender, last_place, latitude,
                longitude, other_information, zodiac_sign)

    print("\nPersona Agregada Con Existo!")
    print(f"""\n\n
    Fecha : {born_date}
    Nombre: {name}
    Apellido: {last_name}
    Genero: {gender}
    Ultimo lugar: {last_place}
    Latitud: {latitude}
    Longitud: {longitude}
    Zodiaco: {zodiac_sign}
    Otra informacion: {other_information}
    """)

    print("""
    0.Volver A Menu De Inicio
    1.Agregar Otro Persona
    2.Modificar Desaparecido
    3.Salir
    """)
    play_sound(adding_last_sound)
    option = int(ask_number("Escribe Tu Opcion: "))

    if option == 0:
        Menu()
    if option == 1:
        add_missing_person()
    elif option == 2:
        modify_missing_person()
    else:
        return


def modify_missing_person():
    system('cls')
    print("A QUIEN QUIERES MODIFICAR ?\n")
    if os.path.isfile("missing_people_db.csv"):
        storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
        for i in range(len(storaged_data)):
            storaged_data[i].remove(i)

        print("\nLISTA DE PERSONAS DESAPARECIDAS")
        print("---------------------------------")

        for person in range(len(storaged_data)):
            print(
                f"{person}) {storaged_data[person][0]}|{storaged_data[person][1]}|{storaged_data[person][2]}|{storaged_data[person][3]}|{storaged_data[person][4]}|{storaged_data[person][5]}|{storaged_data[person][6]}|{storaged_data[person][7]}")

        play_sound(person_chosen_to_modify_sound)
        print("\nELIGE EL NUMERO DE LA PERSONA QUE QUIERES MODIFICAR")
        print("--------------------------------------------------------")
        index_person_to_modify = int(ask_number("Escribe Tu Opcion: "))

        while index_person_to_modify > len(storaged_data) - 1:
            print(
                f'El {index_person_to_modify} no se encuentra en la lista; Elija Uno Que Si Este!')
            play_sound(invalid_option_sound)
            index_person_to_modify = int(ask_number("Escribe Tu Opcion: "))

        person_to_modify = storaged_data[index_person_to_modify]
        system('cls')
        print("\nDATOS DE LA PERSONA ELEGIDA")
        print("--------------------------------")

        print(f"""
        Fecha : {person_to_modify[0]}
        Cedula : {person_to_modify[1]}
        Nombre: {person_to_modify[2]}
        Apellido: {person_to_modify[3]}
        Genero: {person_to_modify[4]}
        Ultimo lugar: {person_to_modify[5]}
        Latitud: {person_to_modify[6]}
        Longitud: {person_to_modify[7]}
        Otra informacion: {person_to_modify[8]}
        """)

        print("\nQUE QUIERES MODIFICAR DE ESTA PERSONA?")
        print("----------------------------------------")
        print("""
        1)Fecha 2)Cedula 3)Nombre 4)Apellido 5)Genero
        6) Ultimo Lugar 7) Latitud 8) Longitud 9) Otra Info """)

        play_sound(data_to_modify_sound)
        print("\nDIGITA EL NUMERO DEL DATO A MODIFICAR")
        data_index_to_modify = ask_number("Escribe Tu Opcion: ")

        while data_index_to_modify > 9:
            print(f"El {data_index_to_modify} no es una opcion; Elija Una!")
            play_sound(invalid_option_sound)
            data_index_to_modify = ask_number("Escribe Tu Opcion: ")

        play_sound(write_new_data_sound)
        person_to_modify[data_index_to_modify -
                         1] = input("Escribe el nuevo dato: ")

        system('cls')
        print("\nDATO MODIFICADO CON EXISTO!")
        print("--------------------------------")
        print(f"""\n\n
        Fecha : {person_to_modify[0]}
        Cedula : {person_to_modify[1]}
        Nombre: {person_to_modify[2]}
        Apellido: {person_to_modify[3]}
        Genero: {person_to_modify[4]}
        Ultimo lugar: {person_to_modify[5]}
        Latitud: {person_to_modify[6]}
        Longitud: {person_to_modify[7]}
        Otra informacion: {person_to_modify[8]}
        """)

        # Here I Updated the datas storage with new one
        dataFrame = pd.DataFrame(storaged_data, columns=[
            "Fecha", "Cedula", "Nombre", "Apellidos", "Genero", "UltimoLugar", "Latitud", "Longitud", "Otra informacion", "Zodiaco"])
        dataFrame.to_csv("missing_people_db.csv")
        print("\n----------------------------------------")
        print("Persona modificada exitosamente!")
        print("----------------------------------------")

        print("""
        0.Volver A Menu De Inicio
        1.Agregar Desaparecido
        2.Modificar Desaparecido
        3.Salir
        """)

        play_sound(modifying_last_sound)
        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
            play_sound(invalid_option_sound)

            option = int(ask_number("Escribe Tu Opcion: "))

        if option == 0:
            Menu()
        elif option == 1:
            add_missing_person()
        elif option == 2:
            modify_missing_person()
        else:
            return
    else:
        print("No hay Ningun Dato Agregado!")
        input("Presione cualquier tecla para volver al menu")
        Menu()


def return_tag(storaged_data):
    for person in range(len(storaged_data)):
        tag = f"""
            <div class="datas">
                <span><span>Fecha:</span>{storaged_data[person][0]}</span>
                <span><span>Cedula:</span>{storaged_data[person][1]}</span>
                <span><span>Nombre:</span> {storaged_data[person][2]}</span>
                <span><span>Apellido:</span>{storaged_data[person][3]}</span>
                <span><span>Genero:</span>{storaged_data[person][4]}</span>
                <span><span>Ultimo Lugar:</span>{storaged_data[person][5]}</span>
                <span><span>Latitud:</span> {storaged_data[person][6]}</span>
                <span><span>Longitud:</span> {storaged_data[person][7]}</span>
                <span><span>Otra Info:</span>{storaged_data[person][8]}</span>
            </div>"""
        tags.append(tag)


def return_li_tag(storaged_data):
    for person in range(len(storaged_data)):
        # here I take from the storaged data the name and last_name of the person
        tag = f"""
            <li>{storaged_data[person][2]} {storaged_data[person][3]}</li>
            """
        li_tag.append(tag)


def return_li_tag_with_zodiac(storaged_data):
    for person in range(len(storaged_data)):
        # here I take from the storaged data the name and last_name of the person
        tag = f"""
            <li>{storaged_data[person][2]} {storaged_data[person][3]} <b>{storaged_data[person][9]}</b></li>
            """
        li_tag_with_zodiac.append(tag)


def export_missing_person_data():
    if os.path.isfile("missing_people_db.csv"):
        storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
        for i in range(len(storaged_data)):
            storaged_data[i].remove(i)

        return_tag(storaged_data)
        html = f"""<!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Lista De Desaparecidos</title>
                <link rel="stylesheet" href="style.css">
            </head>

            <body>
                <h1>Lista De Desaparecidos</h1>
                <div class="container">
                    {" ".join(tags)}
                </div>
            </body>

            </html>
        """

        html_style = """
            * {
                margin: 0;
                padding: 0;
            }

            html,
            body {
                max-height: 100%;
            }

            body {
                background: linear-gradient(45deg, #2a6f8a, #227a51 100%);
            }
            h1 {
                margin-top: 30px;
                color: white;
                text-align: center;
                text-shadow: -2px -2px 10px black;
                font-size: 2.5em;
            }
            .container {
                position: absolute;
                display: flex;
                flex-wrap: wrap;
                top: 20%;
                left: 50%;
                transform: translateX(-50%);
                width: 800px;
                border: 2px solid white;
                padding: 10px;
                border-radius: 15px;
                background: #ffffff1a;
            }

            .container .datas {
                position: relative;
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                border: 1px solid #ffffff71;
                border-radius: 15px;
                margin: 10px 10px;
                background: #ffffff1a;
            }
            .container .datas:hover {
                border: 1px solid #ffffffe8;
            }
            .datas > span {
                width: fit-content;
                height: 50px;
                margin: 10px auto;
                color: white;
                font-weight: bolder;
                padding: 50px auto;
            }
            .datas > span:last-child {
                width: fit-content;
                margin: 10px auto;
            }

            .datas > span > span {
                color: lawngreen;
            }
        """

        os.makedirs("DatosDeDesaparecidos", exist_ok=True)

        style_file = open("DatosDeDesaparecidos/style.css", "w")
        style_file.write(html_style)
        style_file.close()

        html_file = open("DatosDeDesaparecidos/desaparecidos.html", "w")
        html_file.write(html)
        html_file.close()

        wb.open_new_tab("DatosDeDesaparecidos/desaparecidos.html")

        print("\n Sea generado una carpeta con la lista de los desaparecidos\n en la ruta donde esta el archivo .py")
        print("""\n
        1.Volver A Menu De Inicio
        2.Agregar Desaparecido
        3.Salir
        """)

        play_sound(file_generate_sound)

        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
            play_sound(invalid_option_sound)
            option = int(ask_number("Escribe Tu Opcion: "))

        if option == 1:
            Menu()
        elif option == 2:
            add_missing_person()
        else:
            return
    else:
        print("No hay Ningun Dato Agregado!")
        play_sound(not_data_sound)
        input("Presione cualquier tecla para volver al menu")
        Menu()


def show_list_of_missing_person():
    if os.path.isfile("missing_people_db.csv"):
        storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
        for i in range(len(storaged_data)):
            storaged_data[i].remove(i)

        return_li_tag(storaged_data)
        html = f"""<!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Lista De Desaparecidos</title>
                <link rel="stylesheet" href="style.css">
            </head>

            <body>
                <h1>Lista De Desaparecidos</h1>
                <div class="container">
                    <ol class="datas">
                    {" ".join(li_tag)}
                    </ol>
                </div>
            </body>

            </html>
        """

        html_style = """
            * {
            margin: 0;
            padding: 0;
            }

            html,
            body {
            max-height: 100%;
            }

            body {
            background: linear-gradient(45deg, #2a6f8a, #227a51 100%);
            }
            h1 {
            margin-top: 30px;
            color: white;
            text-align: center;
            text-shadow: -2px -2px 10px black;
            font-size: 2.5em;
            text-decoration: underline;
            }
            .container {
            position: absolute;
            display: flex;
            flex-wrap: wrap;
            top: 15%;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            border: 2px solid white;
            border-radius: 5px;
            border-top-right-radius: 50px;
            padding: 30px;
            background: #ffffff1a;
            }

            .container .datas {
            position: relative;
            width: 100%;
            border: 1px solid #ffffff71;
            border-radius: 15px;
            border-right-color: transparent;
            border-top-right-radius: 0px;
            background: #ffffff1a;
            padding: 10px;
            }
            .container .datas:hover {
            border: 1px solid #ffffffe8;
            }

            .datas > li {
            width: 88%;
            margin: 10px 30px;
            color: white;
            font-weight: bolder;
            font-size: 1.2em;
            border: 1px solid #ffffff5e;
            border-radius: 15px;
            border-bottom-left-radius: 2px;
            border-top-left-radius: 2px;
            background: #2a6f8a8c;
            text-align: center;
            height: fit-content;
            transition: margin .2s ease-in-out;
            }
            .datas > li:hover {
            border: 1px solid #ffffffe0;
            margin-left: 15px;
            background: #359fc98c;
            }
        """

        os.makedirs("ListaDeDesaparecidos", exist_ok=True)

        style_file = open("ListaDeDesaparecidos/style.css", "w")
        style_file.write(html_style)
        style_file.close()

        html_file = open("ListaDeDesaparecidos/lista.html", "w")
        html_file.write(html)
        html_file.close()
        wb.open("ListaDeDesaparecidos/lista.html")

        print("\n Sea generado una carpeta con la lista de los desaparecidos\n en la ruta donde esta el archivo .py")
        print("""\n
        1.Volver A Menu De Inicio
        2.Agregar Desaparecido
        3.Salir
        """)

        play_sound(file_generate_sound)

        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
            play_sound(invalid_option_sound)
            option = int(ask_number("Escribe Tu Opcion: "))

        if option == 1:
            Menu()
        elif option == 2:
            add_missing_person()
        else:
            return
    else:
        print("No hay Ningun Dato Agregado!")
        input("Presione cualquier tecla para volver al menu")
        Menu()


def show_list_of_zodiac_with_person_name():
    system('cls')
    print("Numero De Desaparecido Por Signo Del Zodiaco")
    sign_data = []
    signs_counter = [["capricornio", 0], ["Acuario", 0], ["Piscis", 0], ["Aries", 0], ["Tauro", 0], ["Geminis", 0],
                     ["Cancer", 0], ["Leo", 0], ["Virgo", 0], ["Libra", 0], ["Escorpio", 0], ["Saegitario", 0]]

    if os.path.isfile("missing_people_db.csv"):
        storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
        for i in range(len(storaged_data)):
            storaged_data[i].remove(i)
        for person in storaged_data:
            sign_data.append(person[9])

        amount_of_mission_person = len(sign_data)

        print(f"\nEl Total De Desaparecidos es: {amount_of_mission_person}\n")

        return_li_tag_with_zodiac(storaged_data)
        html = f"""<!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Lista De Desaparecidos</title>
                <link rel="stylesheet" href="style.css">
            </head>

            <body>
                <h1>Lista De Desaparecidos</h1>
                <div class="container">
                    <ol class="datas">
                    {" ".join(li_tag_with_zodiac)}
                    </ol>
                </div>
            </body>

            </html>
            """

        html_style = """
            * {
            margin: 0;
            padding: 0;
            }

            html,
            body {
            max-height: 100%;
            }

            body {
            background: linear-gradient(45deg, #2a6f8a, #227a51 100%);
            }
            h1 {
            margin-top: 30px;
            color: white;
            text-align: center;
            text-shadow: -2px -2px 10px black;
            font-size: 2.5em;
            text-decoration: underline;
            }
            .container {
            position: absolute;
            display: flex;
            flex-wrap: wrap;
            top: 15%;
            left: 50%;
            transform: translateX(-50%);
            width: 400px;
            border: 2px solid white;
            border-radius: 5px;
            border-top-right-radius: 50px;
            padding: 30px;
            background: #ffffff1a;
            }

            .container .datas {
            position: relative;
            width: 100%;
            border: 1px solid #ffffff71;
            border-radius: 15px;
            border-right-color: transparent;
            border-top-right-radius: 0px;
            background: #ffffff1a;
            padding: 10px;
            }
            .container .datas:hover {
            border: 1px solid #ffffffe8;
            }

            .datas > li {
            width: 88%;
            margin: 10px 30px;
            color: white;
            font-weight: bolder;
            font-size: 1.2em;
            border: 1px solid #ffffff5e;
            border-radius: 15px;
            border-bottom-left-radius: 2px;
            border-top-left-radius: 2px;
            background: #2a6f8a8c;
            text-align: center;
            height: fit-content;
            transition: margin .2s ease-in-out;
            }
            .datas > li:hover {
            border: 1px solid #ffffffe0;
            margin-left: 15px;
            background: #359fc98c;
            }
            li > b {
            float: right;
            border-left: 2px solid white;
            padding-left: 10px;
            padding-right: 10px;
            background: #ffffff7c;
            border-radius: 15px;
            }
        """

        os.makedirs("ListaConZodiaco", exist_ok=True)

        style_file = open("ListaConZodiaco/style.css", "w")
        style_file.write(html_style)
        style_file.close()

        html_file = open("ListaConZodiaco/listaZodiaco.html", "w")
        html_file.write(html)
        html_file.close()

        wb.open("ListaConZodiaco/listaZodiaco.html")

        for i in range(len(signs_counter)):
            for sign in sign_data:
                if sign == signs_counter[i][0]:
                    signs_counter[i][1] = signs_counter[i][1] + 1

        for data in signs_counter:
            print(f"{data[0]}: {data[1]}")

        print("\n Sea generado una carpeta con la lista de los desaparecidos con su zodiaco\n en la ruta donde esta el archivo .py")
        print("""\n
        1.Volver A Menu De Inicio
        2.Agregar Desaparecido
        3.Salir
        """)

        play_sound(list_zodiac_sound)

        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
            play_sound(invalid_option_sound)
            option = int(ask_number("Escribe Tu Opcion: "))

        if option == 1:
            Menu()
        elif option == 2:
            add_missing_person()
        else:
            return
    else:
        print("No hay Ningun Dato Agregado!")
        input("Presione cualquier tecla para volver al menu")
        Menu()


def generateMap():
    storaged_data = pd.read_csv("missing_people_db.csv").values.tolist()
    for i in range(len(storaged_data)):
        storaged_data[i].remove(i)

    lt = 18.735693
    ln = -70.162651

    map = folium.Map(location=[lt, ln], zoom_start=10)

    fg = folium.FeatureGroup('my map')

    for person in storaged_data:
        fg.add_child(folium.Marker(
            location=[person[6], person[7]], popup=f'<b>{person[2] + " " + person[3]}</b>'))
        map.add_child(fg)

    map.save('map.html')
    wb.open("map.html")

    print("\n Sea generado una archivo con el mapa de los desaparecidos\n en la ruta donde esta el archivo .py")
    print("""\n
    1.Volver A Menu De Inicio
    2.Agregar Desaparecido
    3.Salir
    """)

    play_sound(map_generate_sound)

    option = int(ask_number("Escribe Tu Opcion: "))
    while option > 3:
        print("Elija Una Opcion Validad")
        play_sound(invalid_option_sound)
        option = int(ask_number("Escribe Tu Opcion: "))

    if option == 1:
        Menu()
    elif option == 2:
        add_missing_person()
    else:
        return


def get_zodiac(day, month):
    signs = ("capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis",
             "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Saegitario")
    dates = (20, 19, 20, 20, 20, 21, 22, 23, 22, 22, 22, 21)

    mes = month - 1
    if day > dates[mes]:
        mes + 1
    if mes == 12:
        mes = 0

    zodiac_sign = signs[mes]
    return zodiac_sign


def Menu():
    system('cls')
    print(TITLE)
    print("""
    1.Agregar Desaparecido 
    2.Modificar Desaparecido
    3.Exportar Desaparecido
    4.Mostrar Mapa Desaparecido 
    5.Lista De Desaparecido
    6.Lista De Desaparecido Con Zodiaco
    7.Repetir Opciones
    8.Salir
    """)
    play_sound(menu_sound)

    option = int(ask_number("Escribe Tu Opcion: "))

    while option > 8:
        print(f"El {option} No Es Una Opcion; Elige Una Opcion!")
        play_sound(invalid_option_sound)
        option = int(ask_number("Escribe Tu Opcion: "))

    if option == 1:
        add_missing_person()
    elif option == 2:
        modify_missing_person()
    elif option == 3:
        export_missing_person_data()
    elif option == 4:
        generateMap()
    elif option == 5:
        show_list_of_missing_person()
    elif option == 6:
        show_list_of_zodiac_with_person_name()
    elif option == 7:
        Menu()
    else:
        return


get_from_csv()
Menu()

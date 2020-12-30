# Tarea 6: Programa para registrar
# datos de personas desaparecidas

# Nombre: Luis Alejandro Martinez
# Matricula: 2019-7725

import os
from os import system
import pandas as pd

TITLE = "Programa para registrar datos de personas desaparecidas\n"
SPACE = "    "

data = []


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


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es una  opcione validad; Elija Una!\n")
        ask_number(txt)

    return number


def is_adult(age):
    age = int((age.split("/")[2]))

    if 2020 - age > 17:
        return True
    else:
        return False


def save_to_csv(date, id, name,  last_name, gender, last_place, latitude, longitude, other_information):
    data.append([date, id, name,  last_name, gender, last_place,
                 latitude, longitude, other_information])

    dataFrame = pd.DataFrame(data, columns=[
                             "Fecha", "Cedula", "Nombre", "Apellidos", "Genero", "UltimoLugar", "Latitud", "Longitud", "Otra informacion"])
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
    born_date = ask_data("Escriba Su fecha de nacimineto (Ej: dia/mes/año): ")

    adult = is_adult(born_date)

    if adult:
        id = ask_data("Digita Su Cedula: ")
    else:
        id = "No Posee"

    name = ask_data("Escribe Su Nombre: ")
    last_name = ask_data("Escribe Su Apellido: ")
    gender = ask_data("Escribe Su Genero(M/F): ")
    last_place = ask_data("Escribe El Ultimo Lugar Donde Fue Visto: ")
    latitude = ask_data("Digita La latitud: ")
    longitude = ask_data("Digita La longitud: ")
    other_information = ask_data("Otra informacion: ")

    save_to_csv(born_date, id, name, last_name, gender, last_place, latitude,
                longitude, other_information)

    print("\nPersona Agregada Con Existo!")
    print(f"""\n\n
    Fecha : {born_date}
    Nombre: {name}
    Apellido: {last_name}
    Genero: {gender}
    Ultimo lugar: {last_place}
    Latitud: {latitude}
    Longitud: {longitude}
    Otra informacion: {other_information}
    """)

    print("""
    0.Volver A Menu De Inicio
    1.Agregar Otro Persona
    2.Modificar Desaparecido
    3.Salir
    """)
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

        print("\nELIGE EL NUMERO DE LA PERSONA QUE QUIERES MODIFICAR")
        print("--------------------------------------------------------")
        index_person_to_modify = int(ask_number("Escribe Tu Opcion: "))

        while index_person_to_modify > len(storaged_data) - 1:
            print(
                f'El {index_person_to_modify} no se encuentra en la lista; Elija Uno Que Si Este!')
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

        print("\nDIGITA EL NUMERO DEL DATO A MODIFICAR")
        data_index_to_modify = ask_number("Escribe Tu Opcion: ")

        while data_index_to_modify > 9:
            print(f"El {data_index_to_modify} no es una opcion; Elija Una!")
            data_index_to_modify = ask_number("Escribe Tu Opcion: ")

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
            "Fecha", "Cedula", "Nombre", "Apellidos", "Genero", "UltimoLugar", "Latitud", "Longitud", "Otra informacion"])
        dataFrame.to_csv("missing_people_db.csv")
        print("\n----------------------------------------")
        print("Persona modificada exitosamente!")
        print("----------------------------------------")

        print("""
        1.Volver A Menu De Inicio
        2.Agregar Desaparecido
        3.Salir
        """)
        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
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


tags = []


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

        os.makedirs("listaDeDesaparecidos", exist_ok=True)

        style_file = open("listaDeDesaparecidos/style.css", "w")
        style_file.write(html_style)
        style_file.close()

        html_file = open("listaDeDesaparecidos/desaparecidos.html", "w")
        html_file.write(html)
        html_file.close()

        print("\n Sea generado una carpeta con la lista de los desaparecidos\n en la ruta donde esta el archivo .py")
        print("""\n
        1.Volver A Menu De Inicio
        2.Agregar Desaparecido
        3.Salir
        """)
        option = int(ask_number("Escribe Tu Opcion: "))
        while option > 3:
            print("Elija Una Opcion Validad")
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


def Menu():
    system('cls')
    print(TITLE)
    print("""
    1.Agregar Desaparecido
    2.Modificar Desaparecido
    3.Exportar Desaparecido
    4.Salir
    """)
    option = int(ask_number("Escribe Tu Opcion: "))

    while option > 4:
        print(f"El {option} No Es Una Opcion; Elige Una Opcion!")
        option = int(ask_number("Escribe Tu Opcion: "))

    if option == 1:
        add_missing_person()
    elif option == 2:
        modify_missing_person()
    elif option == 3:
        export_missing_person_data()
    else:
        return


get_from_csv()
Menu()

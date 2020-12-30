# Nombre: Luis Alejandro Martinez
# Matricula: 2019-7725

import requests
import json
import os
from os import system

url = "http://173.249.49.169:88/api/test/consulta/"

signo = ("capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis",
         "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Saegitario")
fechas = (20, 19, 20, 20, 20, 21, 22, 23, 22, 22, 22, 21)


def generate_html(names, last_name, b_day, b_place, zodiac_sign, photo_url):
    os.makedirs(names, exist_ok=True)

    html = f"""
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Information</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>Personal Information</h1>
    <div class="container">
        <div class="data">
            <img src="{photo_url}" alt="foto">
            <span>Nombre: {names}</span>
            <span>Apellido:{last_name}</span>
            <span>Fecha de Nacimiento: {b_day}</span>
            <span>Lugar de Nacimiento: {b_place}</span>
            <span>Zodiao: { zodiac_sign}</span>
        </div>
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
	height: 100%;
}

body {
	background: lightblue;
}
h1 {
	text-align: center;
}
.container {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	max-width: 600px;
	border: 2px solid white;
	border-radius: 15px;
}

img {
	width: 150px;
	margin: 0 auto;
}

.data {
	display: grid;
	max-width: 400px;
	padding: 10px;
	margin: auto 10px;
	text-align: center;
}

span {
	border: 2px solid white;
	padding: 5px 5px;
	border-radius: 15px;
	margin: 10px;
	font-weight: bolder;
}

"""

    file = open(f"{names}/{names}.html", "w")
    file.write(html)
    file.close()

    file2 = open(f"{names}/style.css", "w")
    file2.write(html_style)
    file2.close()

    print("Sean ha gereado su archivo html en la carpeta donde esta el ejecutable .py")


def get_information():
    system('cls')
    print("Programa que acpeta una cedula y genera un archivo html cons la informacion")

    id = input("Digite su numero de cedula: ")
    try:
        response = requests.get(url + id)
        data = response.json()

        if data["Ok"] == True:
            names = data["Nombres"]

            if type(data["Apellido2"]) == str:
                last_name = data["Apellido1"] + " " + data["Apellido2"]
            else:
                last_name = data["Apellido1"]

            b_day = data["FechaNacimiento"].split()[0]
            b_place = data["LugarNacimiento"]

            photo_url = data["Foto"]

            day = int(b_day.split("-")[2])
            month = int(b_day.split("-")[1])

            mes = month - 1
            if day > fechas[mes]:
                mes + 1
            if mes == 12:
                mes = 0

            zodiac_sign = signo[mes]

            print(f"""
            Nombre = {names}
            Apellidos = {last_name}
            Fecha de nacimiento = {b_day}
            Lugar de Nacimiento = {b_place}
            Zodiaco = {zodiac_sign}
            """)

            generate_html(names, last_name, b_day,
                          b_place, zodiac_sign, photo_url)

        else:
            print("La cedula no existe!")

    except requests.ConnectionError:
        print("No tiene conexion!")


get_information()

input("Presiona cualquier tecla para salir...")


# Nombre: Luis Alejandro Martinez
# Matricula: 2019-7725

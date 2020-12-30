import requests
import json
import os

url = "https://periodic-table-api.herokuapp.com/atomicSymbol/"
title = """\n
********************************************************
*  programa que acepta el codigo de un elemento        *
*  de la tabla periodica y genera un archivo html      *
*  donde muestra los datos siguientees:                *
*  nombre, numero atomico, estado de la materia.       *
********************************************************
\n"""

os.system('cls')


def generate_html(element_name, element_atomic_number, element_standard_state):
    html = f"""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>ELEMENT'S INFORMATION</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <div class="container">
            <h1>ELEMENT'S INFORMATION</h1>
            <br>

            <div class="data">
                <label for="name" >Nombre: {element_name}</label>
                <label for="atomicNumber" >Numero Atomico: {element_atomic_number}</label>
                <label for="standardState">Estado en la Materia: {element_standard_state }</label>
            </div>
        </div>
    </body>

    </html>
    """

    html_style = """
    body {
	background: rgb(30, 41, 46);
	font-family: sans-serif;
    }

    .container {
    	color: rgb(255, 255, 255);
    	text-align: center;
    	max-width: 600px;
    	margin: 30px auto;
    }
    .data {
    	display: grid;
    	padding: 14px 0;
    	max-width: 300px;
    	margin: auto 25%;
    	text-align: justify;
    	border: 1px solid #ddd;
    	background: #083271;
    }
    label {
    	position: relative;
    	padding: 10px;
    }
    """

    os.makedirs(f"{element_name}", exist_ok=True)

    style_file = open(f"{element_name}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(f"{element_name}/{element_name}'s_information.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con el nombre del elemento que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def get_element():
    print(title)

    element = input("Escribe el simbolo del elemento: ")

    try:
        response = requests.get(url + element, timeout=5)
        data = response.json()

        if len(data) == 2:
            print(f"""\n
    ------------------------------------------------------
                    EL ELEMENTO NO EXISTE!
    ------------------------------------------------------
        """)
        else:
            element_name = data["name"]
            element_atomic_number = data["atomicNumber"]
            element_standard_state = data["standardState"]

            print(f"""
            ----------------------
            | Nombre | {element_name}   |
            ----------------------
            | Numero Atomico | {element_atomic_number} |
            ------------------------------
            | Estado En La Materia | {element_standard_state} | 
            ------------------------------
            """)

            generate_html(element_name, element_atomic_number,
                          element_standard_state)

    except requests.ConnectionError:
        print(f"""\n
    ------------------------------------------------------
                    NO TIENES CONEXION!
    ------------------------------------------------------
        """)

    input("\nPrsione cualquier tecla para salir...")


get_element()

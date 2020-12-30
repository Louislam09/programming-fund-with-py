# Programa que al abrir le tire una foto
# al usuario solicite el nombre, apellido  y
# luego genere un archivo HTML con los datos.

from cv2 import *
from os import system
import time

title = """
********************************************************
    Programa que al abrir le tire una foto 
    al usuario solicite el nombre, apellido  y
    luego genere un archivo HTML con los datos. 
********************************************************
"""


def generate_html(name, lastname, img_url):
    html = f"""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>INFORMACION CON FOTO</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <div class="container">
            <h1>INFORMACION CON FOTO</h1>
            <br>
            <div class="data" >
                <img src={img_url} class="img" width="250">
                <br>
                <label for="name">Nombre: {name}</label>
                <label for="lastname" >Apellido: {lastname}</label>
            </div>
        </div>

    </body>

    </html>
    """
    html_style = """
       html,
    body {
    	height: 100%;
    	overflow: hidden;
    }

    body {
    	background: repeating-linear-gradient(180deg, #245166, #341f77 100%);
    	font-family: sans-serif;
    }

    .container {
    	color: #fff;
    	text-align: center;
    	max-width: 600px;
    	margin: 30px auto;
    }
    h1 {
    	text-shadow: -8px 6px 5px #000;
    }

    .data {
    	display: grid;
    	padding: 30px 0;
    	max-width: 300px;
    	margin: auto 25%;
    	text-align: justify;
    	border: 1px solid #ddd;
    	background: #ffffff15;
    	border-radius: 15px;
    	transition: .4s;
    }
    label {
    	position: relative;
    	padding: 15px;
    	font-size: 2em;
    	margin: 10px auto;
    	text-shadow: -8px 6px 5px #000;
    	border-top: 1px solid white;
    	border-bottom: 1px solid white;
    	background: #ffffff15;
    	border-radius: 15px;
    }

    .img {
    	margin: auto;
    	border-top: 2px solid white;
    	border-radius: 15px;
    	border-bottom: 2px solid white;
    	transition: .4s;
    }

    .data:hover {
    	border: 2px solid #fff;
    }
    img:hover {
    	transform: scale(1.1);
    	cursor: pointer;
    }
    label:hover {
    	text-shadow: -8px 6px 30px blue;
    	transform: translateX(5px);
    }
    """

    style_file = open(f"{name}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(f"{name}/{name}'s_information.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con el nombre  que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def take_pic(name):
    camara = VideoCapture(0)
    s, img = camara.read()

    if s:
        imshow("camara", img)
        waitKey(4150)
        destroyWindow("camara")
        imwrite(f"{name}/{name}.png", img)


def start_program():
    system('cls')
    print(title)

    try:
        name = input("Escribe tu nombre: ")
        lastname = input("Escribe tu apellido: ")
        img_url = f"{name}.png"

        os.makedirs(f"{name}", exist_ok=True)

        print("\nTe tomara un foto en unos segundos")

        take_pic(name)
        system('cls')

        generate_html(name, lastname, img_url)

        print("\nQuieres otra foto?")
        option = input("\n1) Si \n2) No y terminar.\n-opcion: ")
        if option == "1":
            start_program()
        else:
            system("exit")

    except:
        print("\nHubo un problema, prueba de nuevo!")


start_program()


time.sleep(3)
print("\nPresiona  cualquier tecla para salir....")
input()

# Programa que acepta un numero y Genera la tabla de multiplicar
#  de dicho numero hasta el diez. Luego te dara un archivo html con
#  una tabla donde aparecera dicha tabla de multiplicar de dos forma
# Ejemplo:
# 1x1   uno por uno
# 1x2   uno por dos
# 1x3   uno por tres

import os

title = """
************************************************************************
    Programa que acepta un numero 1 al 10 y Genera la tabla de multiplicar
    de dicho numero hasta el diez. Luego te dara un archivo html con
    una tabla donde aparecera dicha tabla de multiplicar de dos forma
************************************************************************
"""


number_1_to_20_name = [
    'UNO',
    'DOS',
    "TRES",
    "CUATRO",
    "CINCO",
    "SEIS",
    "SIETE",
    "OCHO",
    "NUEVE",
    "DIEZ",
    "ONCE",
    "DOCE",
    "TRECE",
    "CATORCE",
    "QUINCE",
    "DIECISEIS",
    "DIECESIETE",
    "DIECIOCHO",
    "DIECINUEVE",
    "VEINTE"
]

number_10_to_100_name = [
    "DIEZ",
    "VIENTE",
    "TEINTA",
    "CUARENA",
    "CINCUENTA",
    "SESENTA",
    "SETENTA",
    "OCHENTA",
    "NOVENTA",
    "CIEN"
]

number_form = []
letter_form = []


def number_name(number):
    global name

    if number <= 20:
        name = number_1_to_20_name[number-1]
    elif number < 100 and number % 10 == 0:
        name = number_10_to_100_name[int(str(number)[0]) - 1]
    elif number < 100 and number % 10 != 0:
        name = number_10_to_100_name[int(
            str(number)[0]) - 1] + " Y " + number_1_to_20_name[int(str(number)[1]) - 1]
    elif number == 100:
        name = number_10_to_100_name[len(number_10_to_100_name)-1]


def multiply_number(num):
    print(f"TABLA DEL MULTIPLICAR DEL NUMERO {num} HASTA EL 10")

    for i in range(10):
        multiplier = i + 1
        print(f"{multiplier} X {num} = {multiplier*num}")
        number_form.append(f"{multiplier} X {num} = {multiplier*num}")

    print("\n")
    for i in range(10):
        multiplier = i + 1
        number_name(multiplier * num)

        print(
            f"{number_1_to_20_name[multiplier-1]} POR {number_1_to_20_name[num-1]} = {name}")
        letter_form.append(
            f"{number_1_to_20_name[multiplier-1]} POR {number_1_to_20_name[num-1]} = {name}")


def generate_html(number_for_multiply):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicio 3 |Tabla De Multiplicar</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <h1>Tabla de Multiplicar Del Numbero {number_for_multiply} Hasta El 10</h1>
        <div class="container">
            <section class="number-side">
                <span>{number_form[0]}</span>
                <span>{number_form[1]}</span>
                <span>{number_form[2]}</span>
                <span>{number_form[3]}</span>
                <span>{number_form[4]}</span>
                <span>{number_form[5]}</span>
                <span>{number_form[6]}</span>
                <span>{number_form[7]}</span>
                <span>{number_form[8]}</span>
                <span>{number_form[9]}</span>
            </section>

            <section class="letter-side">
                <span>{letter_form[0]}</span>
                <span>{letter_form[1]}</span>
                <span>{letter_form[2]}</span>
                <span>{letter_form[3]}</span>
                <span>{letter_form[4]}</span>
                <span>{letter_form[5]}</span>
                <span>{letter_form[6]}</span>
                <span>{letter_form[7]}</span>
                <span>{letter_form[8]}</span>
                <span>{letter_form[9]}</span>

            </section>

        </div>
    </body>

    </html>
        """

    html_style = """
            * {
    	margin: 0;
    	padding: 0;
    }

    :root {
    	--container-width: 600px;
    	--container-height: 500px;
    	--text-shadow-color: #f7db17;
    }

    html,
    body {
    	height: 100%;
    }
    body {
    	/* background: repeating-radial-gradient(#11b5a6, #4c469e); */
    	background: repeating-linear-gradient(#4c469e, #11b5a6);
    }

    h1 {
    	text-align: center;
    	color: white;
    	font-size: 2.5em;
    	margin-bottom: 50px;
    	font-weight: bolder;
    	text-shadow: -5px -3px 4px #122379;
    }

    .container {
    	position: absolute;
    	display: flex;
    	flex-direction: row;
    	width: var(--container-width);
    	height: var(--container-height);
    	left: 50%;
    	top: 55%;
    	transform: translate(-50%, -50%);
    	border-radius: 15px;
    	border: 2px solid white;
    	padding: 10px;
    }

    .number-side {
    	display: flex;
    	flex-direction: column;
    	width: 20%;
    	border: 2px solid white;
    	text-align: center;
    	color: white;
    	border-radius: 15px;
    	background: white;
    	padding: 10px 10px;
    	font-weight: bolder;
    	margin: 10px 20px;
    	background: repeating-linear-gradient(240deg, #45a296, #95bcd8f2 65%);
    	box-shadow: -6px 7px 10px 0px #11b5a6;
    }

    .number-side > span:hover {
    	border: 2px solid white;
    	transform: translateX(15%);
    }

    .number-side > span {
    	border: 1px solid #d5e4e2;
    	padding: 9px 10px;
    	margin: 4px 10px;
    	font-size: 14px;
    	border-radius: 10px;
    }

    .letter-side {
    	display: flex;
    	flex-direction: column;
    	width: 60%;
    	margin: 10px 10px;
    	border: 2px solid white;
    	text-align: center;
    	color: white;
    	border-radius: 15px;
    	background: white;
    	padding: 5px 10px;
    	font-weight: bolder;
    	background: repeating-linear-gradient(-230deg, #45a296, #95bcd8f2 65%);
    	box-shadow: -6px 7px 10px 0px #11b5a6;
    }

    .letter-side > span:hover {
    	border: 2px solid white;
    	transform: translateX(10%);
    }
    .letter-side > span {
    	font-size: 14px;
    	border: 1px solid #d5e4e2;
    	padding: 9px 10px;
    	margin: 5px 20px;
    	border-radius: 10px;
    }

    """

    os.makedirs(f"tabla_del_{number_for_multiply}", exist_ok=True)

    style_file = open(f"tabla_del_{number_for_multiply}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(
        f"tabla_del_{number_for_multiply}/tabla_del_{number_for_multiply}.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con la tabla de mutiplicar del numero que  ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def start_multiply():
    os.system('cls')
    print(title)

    number_to_multiply = int(input("Digita un numero: "))

    multiply_number(number_to_multiply)
    generate_html(number_to_multiply)
    
    input("Presiona cualquier tecla para salir...")


start_multiply()

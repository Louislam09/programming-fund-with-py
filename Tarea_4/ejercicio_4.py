# 100-90 = A (EXCELENTE)
# 89-80 = B (MUY BUEN0)
# 79-70 = C (BUENO)
# 69-60 = D (POCO SASTIFACTORIO)
# 0-59 = F (MALA)

import os

title = """
********************************************************
    PROGRAMA QUE ACEPTE UNA CALIFICACION Y MUESTRE EL 
    EQUIVALENTE LITERAL (A,B,C o F), LUEGO GENERE UN 
        HTML CON ESOS DATOS DE UNA FORMA ELEGANTE
********************************************************
\n"""


def ask_number(txt):
    try:
        global number
        number = input(txt)
        number = int(number)
    except:
        print(f">>>{number}" + " no es un numero\n")
        ask_number(txt)
    return number


def rank_qualification(number):
    global rank
    global status
    global status_color
    if number >= 90 and number <= 100:
        rank = "A"
        status = "Has Aprobado! Felicidades!"
        status_color = "#00ff4c88"
    elif number >= 80 and number <= 89:
        rank = "B"
        status = "Has Aprobado! Excelente!"
        status_color = "#006eff88"
    elif number >= 70 and number <= 79:
        rank = "C"
        status = "Has Aprobado! Esfuezarte mas!"
        status_color = "#ffe60088"
    else:
        rank = "F"
        status = "Has Reprobado! No rinda!"
        status_color = "#ff0000c4"


def generate_html(name):
    html = f"""
        <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicio 4 | Student Qualification State</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <h1>Ejercicio 4 | Student Qualification State</h1>
        <div class="container">
            <div class="rank-section">
                <span> Tu Calificacion es una <i>{rank}</i></span>
            </div>

            <div class="student-state-section" style="background: {status_color}">
                <span>{status}</span>
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
    	background: repeating-linear-gradient(#00a5e4, #11b562);
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
    	flex-direction: column;
    	width: var(--container-width);
    	height: var(--container-height);
    	left: 50%;
    	top: 55%;
    	transform: translate(-50%, -50%);
    	border-radius: 15px;
    	padding: 10px;
    }
    .container div {
    	background: lightblue;
    	text-align: center;
    	font-size: 3em;
    	color: white;
    	height: 30%;
    	border: 2px solid white;
    	border-radius: 15px;
    	padding-top: 50px;
    	font-weight: bolder;
    	text-shadow: -4px 4px 2px black;
    	margin: 20px 10px;
    }

    .container .rank-section {
    	background: linear-gradient(30deg, #257f9abf, #79c8e0);
    	border: 2px solid rgba(255, 255, 255, 0.637);
    	box-shadow: 0 0 20px 4px #19d6f5;
    }

    .container i {
        text-decoration: underline;
    }

    .container .student-state-section {
    	background: #11b562;
    	box-shadow: 0 0 20px 4px #19d6f5;
    	border: 2px solid rgba(255, 255, 255, 0.637);
    }
    """

    os.makedirs(f"calificacion_de_{name}", exist_ok=True)

    style_file = open(f"calificacion_de_{name}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(f"calificacion_de_{name}/qualification_state.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta llamada caliicacion_de_'nombre ingresado' donde obtendras el resultado de la calificaion que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def start_program():
    os.system("cls")
    print(title)

    name = input("Escribe tu nombre: ")
    qualification = ask_number("Digita tu calificacion: ")
    rank_qualification(qualification)
    generate_html(name)

    
    input("Presiona cualquier tecla para salir...")


start_program()

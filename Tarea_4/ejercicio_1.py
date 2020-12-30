# Programa que acepte nombre, apellido,telefono y
# direccion de una persona y Genere un archio html que
# contenga esta informacion en un formato bonito y elegante.

import os

title = """
=============================================================== 
     Programa que acepta el nombre, apellido, telefono y
    direccion de una persona y Genera un archivo html que
      contiene la informacion en un formato  elegante.
===============================================================
"""


def ask_info(txt):
    resolve = input(txt)

    if len(resolve) > 0:
        return resolve
    else:
        ask_info(txt)


def start_asking_info():
    os.system('cls')
    print(title)
    name = ask_info("Escribe tu nombre: ")
    last_name = ask_info("Escribe tu apellido: ")
    gender = ask_info("Escribe tu genero (M/F): ")
    phone_number = ask_info("Escribe tu numero de telefono: ")
    address = ask_info("Escribe tu direccion: ")

    if gender == "m" or gender == "M":
        image_url = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f9/f9bf4c5727187c3c684523f4a882fbaf0b317610_full.jpg"
    else:
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTAe-c33nTQgMW11q8KYsg432j13PNU1Y7Y1HyLuJqaLOAAilRd&usqp=CAU"

    html = f"""
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 1 | Personal Information</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="container">
        <section class="image-side">
            <img src="{image_url}" alt="photo">
            <span>{name+ " " + last_name}</span>
        </section>

        <section class="info-side">
            <span>Nombre: {name}</span>
            <span>Apellido: {last_name}</span>
            <span>Direccion: {address}</span>
            <span>Telephone: {phone_number}</span>
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
	--container-height: 300px;
}

html,
body {
	height: 100%;
}
body {
	background: repeating-radial-gradient(#11b5a6, #4c469e);
}
.container {
	position: absolute;
	width: var(--container-width);
	height: var(--container-height);
	left: 50%;
	top: 30%;
	transform: translate(-50%, -50%);
	border-radius: 15px;
}

.image-side {
	position: absolute;
	left: 0%;
	/* background: #11b57899; */
	background: repeating-linear-gradient(90deg, #11b57899, darkcyan 5px);
	width: 40%;
	height: 99%;
	border: 1px solid white;
	border-radius: 15px;
	border-bottom-right-radius: 0;
	border-top-right-radius: 0;
}

img {
	position: absolute;
	left: 50%;
	top: 25%;
	transform: translate(-50%, -50%);
	width: 100px;
	height: 100px;
	border: 2px solid white;
	border-radius: 50%;
}

.image-side > span {
	position: absolute;
	left: 50%;
	top: 65%;
	transform: translate(-50%, -50%);
	color: white;
	font-size: 2em;
	text-align: center;
	text-shadow: -6px 4px 20px #49fb00;
}

.info-side {
	position: absolute;
	left: 40%;
	background: darkcyan;
	width: 58%;
	height: 99%;
	border: 1px solid #11b57899;
	border-radius: 15px;
	border-bottom-left-radius: 0;
	border-top-left-radius: 0;
	display: flex;
	flex-direction: column;
}
.info-side > span {
	position: relative;
	padding: 22px 10px;
	margin: 4px 2px;
	font-size: 1.2em;
	border-radius: 15px;
	border-left: 2px solid white;
	border-bottom-left-radius: 0;
	border-top-left-radius: 0;
	color: white;
	font-weight: bolder;
	background: repeating-linear-gradient(45deg, darkcyan, teal 100px);
	text-align: center;
	text-shadow: -2px 0px 15px #49fb00;
}

.info-side > span:hover {
	border: 2px solid white;
	border-left: none;
	margin-left: 10px;
	filter: hue-rotate(15deg);
}
"""

    os.makedirs(f"{name+last_name}/css", exist_ok=True)

    style_file = open(f"{name+last_name}/css/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(f"{name+last_name}/{name}'s_Information.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con el nombre de la persona que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")
    input("Presiona una tecla para cerrar...")


start_asking_info()

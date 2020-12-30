import os

title = """
********************************************************************
      PROGRAMA QUE ACEPTA UNA FECHA DE NACIMIENTO Y UN TIPO DE 
      SANGRE Y GENERA UN ARCHIVO HTML QUE MUESTRA LA FECHA DE LA
      PERSONA, EL SIGNO DEL ZODIACO CON UNA FOTO DEL MISMO, LAS
      PERSONAS DE LA CUALES PUEDE RECIBIR SANGRE Y A CUAELES 
      PUEDE DONAR, MOSTRAR TODO  ESTOS DATOS DE UNA FORMA ELEGANTE
********************************************************************
\n"""


def ask_info(txt):
    resolve = input(txt)

    if len(resolve) > 0:
        return resolve
    else:
        ask_info(txt)


def get_blood_compatibility(blood_type):
    global can_donate
    global can_receive

    if blood_type.upper() == "A+":
        can_donate = "A+ | AB+"
        can_receive = "0+ | 0- | A+ | A- "
    if blood_type.upper() == "A-":
        can_donate = "A+ | AB+ | A- | AB-"
        can_receive = "0- |  A- "
    if blood_type.upper() == "B+":
        can_donate = "B+ | AB+"
        can_receive = "0+ | 0- | B+ | B- "
    if blood_type.upper() == "B-":
        can_donate = "B+ | AB+ | B- | AB-"
        can_receive = " 0- | B- "
    if blood_type.upper() == "AB+":
        can_donate = "AB+"
        can_receive = " TODOS "
    if blood_type.upper() == "AB-":
        can_donate = "AB+ | AB-"
        can_receive = " 0- | B- | AB- | A- "
    if blood_type.upper() == "O+":
        can_donate = "A+ | B+ | AB+ | O+"
        can_receive = "0+ | 0-   "
    if blood_type.upper() == "O-":
        can_donate = " TODOS "
        can_receive = " 0- "


def get_zodiac(day, month):
    global zodiac_sign
    global zodiac_sign_image

    if day > 31 or day <= 0 or month > 12 or month <= 0:
        print("No tienes signo de zodayco porque no eres de este planeta! X'D")
        return
    if (day >= 21 and month == 3 or day <= 20 and month == 4):
        zodiac_sign = "Aries"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/aries.jpg'
    elif (day >= 21 and month == 4 or day <= 21 and month == 5):
        zodiac_sign = "Tauro"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/taurus.jpg'

    elif (day >= 22 and month == 5 or day <= 21 and month == 6):
        zodiac_sign = " Géminis"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/gemini.jpg'

    elif (day >= 22 and month == 6 or day <= 22 and month == 7):
        zodiac_sign = "Cáncer"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/cancer.jpg'

    elif (day >= 23 and month == 7 or day <= 23 and month == 8):
        zodiac_sign = " Leo"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/leo.jpg'

    elif (day >= 24 and month == 8 or day <= 23 and month == 9):
        zodiac_sign = "Virgo"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/virgo.jpg'

    elif (day >= 24 and month == 9 or day <= 23 and month == 10):
        zodiac_sign = " Libra"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/libra.jpg'

    elif (day >= 24 and month == 10 or day <= 22 and month == 11):
        zodiac_sign = "Escorpio"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/scorpio.jpg'

    elif (day >= 23 and month == 11 or day <= 21 and month == 12):
        zodiac_sign = "Sagitario"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/sagittarius.jpg'

    elif (day >= 22 and month == 12 or day <= 20 and month == 1):
        zodiac_sign = "Capricornio"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/capricorn.jpg'

    elif (day >= 21 and month == 1 or day <= 18 and month == 2):
        zodiac_sign = "Acuario"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/aquarius.jpg'

    elif (day >= 19 and month == 2 or day <= 20 and month == 3):
        zodiac_sign = "Piscis"
        zodiac_sign_image = 'https://www.astrology-zodiac-signs.com/images/pisces.jpg'


def generate_html(name, day, month, year, zodiac_sign, zodiac_sign_image, blood_type):
    html = f"""
      <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicio 2 |Zodiac and Blood Compatibilty</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body onload="alert('Pase el cursor por la carta para ver la compartibilidad de sangre')">
        <div class="container">
            <h1>Zodiac and Blood Compatibilty</h1>
            <section class="image-side">
                <img src="{zodiac_sign_image}" alt="{zodiac_sign}">
                <span>Zodiaco: <i>{zodiac_sign.upper()}</i></span>
                <span>Fecha Nac: <i>{day}-{month}-{year}</i></span>
                <span>Tipo De Sangre: <i>{blood_type}</i></span>
            </section>

            <section class="info-side">
                <span>Puede Donar A:</span>
                <p>{can_donate}</p>
                <span>Puede Recibir De:</span>
                <p>{can_receive}</p>
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
    	--text-shadow-color: #f7db17;
    }

    html,
    body {
    	height: 100%;
    }
    body {
    	background: repeating-radial-gradient(#11b5a6, #4c469e);
    	/* background: repeating-linear-gradient(90deg, #46759e, #0e1915fa 5px); */
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
    h1 {
	text-align: center;
	color: white;
	font-size: 2.5em;
	margin-bottom: 30px;
	font-weight: bolder;
	text-shadow: -5px -3px 4px #122379;
    }
    .image-side {
    	position: absolute;
    	left: 0%;
    	background: repeating-radial-gradient(#0b7ff7, #122379);
    	width: 40%;
    	height: 99%;
    	border: 1px solid white;
    	border-radius: 15px;
    	border-bottom-right-radius: 0;
    	border-top-right-radius: 0;
    	display: flex;
    	flex-direction: column;
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
    i {
    	text-decoration: underline;
    	color: #f6f1f1f6;
    }

    .image-side > span {
    	position: relative;
    	top: 45%;
    	padding: 10px 10px;
    	margin: 2px 2px;
    	font-size: 1.4em;
    	color: white;
    	font-weight: bolder;
    	text-align: center;
    	text-shadow: -2px 0px 15px var(--text-shadow-color);
    }

    .image-side:hover ~ .info-side {
    	opacity: 1;
    	left: 40%;
    }
    .image-side:hover {
    	border: 2px solid white;
    }

    .info-side {
    	position: absolute;
    	left: -10%;
    	background: #031444fa;
    	width: 58%;
    	height: 99%;
    	border: 1px solid white;
    	border-radius: 15px;
    	border-bottom-left-radius: 0;
    	border-top-left-radius: 0;
    	display: flex;
    	flex-direction: column;
    	z-index: -1;
    	opacity: 0;
    	transition: .9s;
    }

    .info-side:hover {
    	opacity: 1;
    	left: 40%;
    }

    .info-side > span {
    	position: relative;
    	padding: 22px 10px;
    	margin: 4px 2px;
    	font-size: 1.2em;
    	border-radius: 15px;
    	border: 2px solid white;
    	border-bottom-left-radius: 0;
    	border-bottom-right-radius: 0;
    	border-top-left-radius: 0;
    	color: white;
    	font-weight: bolder;
    	background: repeating-linear-gradient(#057c72, #001080de);
    	/* background: repeating-linear-gradient(45deg, #3656a2, #0d26d6de 5px); */
    	text-align: center;
    	text-shadow: -2px 0px 15px var(--text-shadow-color);
    }

    .info-side > span:hover {
    	border: 2px solid white;
    	border-left: none;
    	margin-left: 10px;
    	filter: hue-rotate(15deg);
    }

    .info-side > p {
    	position: relative;
    	padding: 22px 10px;
    	margin: -4px 2px;
    	font-size: 1.4em;
    	margin-bottom: 4px;
    	border: 2px solid white;
    	border-left: 2px solid white;
    	border-bottom-left-radius: 15px;
    	border-bottom-left-radius: 0;
    	border-top-left-radius: 0;
    	color: white;
    	font-weight: bolder;
    	background: repeating-linaer-gradient(#0b7ff7, #122379);
    	text-align: center;
    	text-shadow: -2px 0px 15px var(--text-shadow-color);
    	background: #2587a5;
    	border-bottom-left-radius: 15px;
    	border-bottom-right-radius: 15px;
    }
    """

    os.makedirs(f"{name}", exist_ok=True)

    style_file = open(f"{name}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(f"{name}/{name}'s_zodiac_blood_compatibility.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con el nombre de la persona que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def start_program():
    os.system('cls')
    print(title)

    name = ask_info('Escribe tu nombre: ')
    day = int(ask_info('Digita tu dia de nacimiento: '))
    month = int(ask_info('Digita tu mes de nacimiento(1-12): '))
    year = int(ask_info('Digita tu año de nacimiento: '))
    blood_type = ask_info('Escribe tu tipo de sangre(A+,A-,AB+,etc...): ')

    get_zodiac(day, month)

    get_blood_compatibility(blood_type)
    generate_html(name, day, month, year, zodiac_sign,
                  zodiac_sign_image, blood_type)

    input("Presiona cualquier tecla para salir...")


start_program()

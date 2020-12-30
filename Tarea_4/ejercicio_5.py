# Programa que acepte una frase y genere un archivo
# html que las contega de las siguientes formas:
# -todas en mayusculas
# -todas en minusculas
# -invertida
# - numerica A: 4, E: 3, I: 1, O: 0, U: 7
# - Invertir el orden de las palabras: hola mundo| mundo hola
import os

title = "PROGRAMA...\n"


def get_upper(frase):
    return frase.upper()


def get_lower(frase):
    return frase.lower()


def get_reverse(frase):
    new_frase = list(frase)
    new_frase.reverse()
    new_frase = "".join(new_frase)

    return new_frase


def get_numberical(frase):
    frase = frase.lower()
    frase = frase.replace("a", "4")
    frase = frase.replace("e", "3")
    frase = frase.replace("i", "1")
    frase = frase.replace("o", "0")
    frase = frase.replace("u", "7")

    return frase


def get_sort(frase):
    new_frase = frase.split(" ")
    new_frase.reverse()
    frase = " ".join(new_frase)

    return frase


def generate_html(upper_frase, lower_frase, reverse_frase, numerical_frase, sort_frase):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicio 5 |Jugar con un String</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <h1>Ejercicio 5 |Jugar con un String</h1>
        <div class="container">
            <section class="letter-side">
                <span>{upper_frase}</span>
                <span>{lower_frase}</span>
                <span>{reverse_frase}</span>
                <span>{numerical_frase}</span>
                <span>{sort_frase}</span>
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
    	background: black;
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
    	width: var(--container-width);
    	height: var(--container-height);
    	left: 50%;
    	top: 55%;
    	transform: translate(-50%, -50%);
    	padding: 10px;
    }
    
    .letter-side {
    	position: absolute;
    	display: flex;
    	flex-direction: column;
    	width: 60%;
    	left: 50%;
    	top: 45%;
    	transform: translate(-50%, -50%);
    	border: 2px solid white;
    	text-align: center;
    	color: white;
    	border-radius: 15px;
    	background: white;
    	padding: 5px 10px;
    	font-weight: bolder;
    	background: repeating-linear-gradient(20deg, #a2458e, #c495d8f2 50%);
    	box-shadow: -6px 7px 20px 0px #4111b591;
    	animation: spinner 10s linear infinite;
    }
    
    @keyframes spinner {
    	0% {
    		background: repeating-linear-gradient(-180deg, #a2458e, #c495d8f2 50%);
    	}
    	10% {
    		background: repeating-linear-gradient(-150deg, #a2458e, #c495d8f2 50%);
    	}
    	20% {
    		background: repeating-linear-gradient(-120deg, #a2458e, #c495d8f2 50%);
    	}
    	30% {
    		background: repeating-linear-gradient(-90deg, #a2458e, #c495d8f2 50%);
    	}
    	40% {
    		background: repeating-linear-gradient(-60deg, #a2458e, #c495d8f2 50%);
    	}
    	50% {
    		background: repeating-linear-gradient(-30deg, #a2458e, #c495d8f2 50%);
    	}
    	60% {
    		background: repeating-linear-gradient(0deg, #a2458e, #c495d8f2 50%);
    	}
    	70% {
    		background: repeating-linear-gradient(-45deg, #a2458e, #c495d8f2 50%);
    	}
    	80% {
    		background: repeating-linear-gradient(-90deg, #a2458e, #c495d8f2 50%);
    	}
    	90% {
    		background: repeating-linear-gradient(-135deg, #a2458e, #c495d8f2 50%);
    	}
    	95% {
    		background: repeating-linear-gradient(-180deg, #a2458e, #c495d8f2 50%);
    	}
    	100% {
    		background: repeating-linear-gradient(-20deg, #a2458e, #c495d8f2 50%);
    	}
    }
    
    .letter-side > span:hover {
    	border: 2px solid white;
    	transform: translateX(10%);
    }
    .letter-side > span {
    	font-size: 25px;
    	border: 1px solid #d5e4e2;
    	padding: 25px 10px;
    	margin: 5px 20px;
    	border-radius: 10px;
    }
    
    """

    os.makedirs(f"{upper_frase[0]}", exist_ok=True)

    style_file = open(f"{upper_frase[0]}/style.css", "w")
    style_file.write(html_style)
    style_file.close()

    html_file = open(
        f"{upper_frase[0]}/{upper_frase[0]}.html", "w")
    html_file.write(html)
    html_file.close()

    print("\n Sea generado una carpeta con la primera palabra de la frase que ha ingresado\n en la ruta donde esta el archivo .py")
    print("\nGracias Por Preferirnos! | :D x'D ")


def start_program():
    os.system('cls')
    print(title)

    frase = input("Escribe una frase: ")

    upper_frase = get_upper(frase)
    lower_frase = get_lower(frase)
    reverse_frase = get_reverse(frase)
    numerical_frase = get_numberical(frase)
    sort_frase = get_sort(frase)

    generate_html(upper_frase, lower_frase, reverse_frase,
                  numerical_frase, sort_frase)
    
    input("Presiona cualquier tecla para salir...")


start_program()

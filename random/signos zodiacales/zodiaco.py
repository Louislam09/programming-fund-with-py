
zodiacales = ("capricornio", "acuario", "piscis", "aries", "tauro",
              "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (21, 19, 20, 20, 21, 20, 21, 22, 23, 22, 23, 22)


dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes: "))
año = int(input("introduce el año: "))

mes = mes - 1

if dia > fechas[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print("Tu signo es: ", zodiacales[mes])

plt = str(input("ingrese su tipo de sangre: ")).upper()
tipo_sangre = {"A+": "puede donar a: A+,B+, puede recibir de: B+,B-,O+,O-", "O+": "puede donar a: A+,O+,B+,AB, puede recibir de: O+,O-",
               "B+": "puede donar a: B+,AB+, puede recibir de: B+,B-,O+,O-", "AB+": "puede donar a: AB+, puede recibir de: todos", "A-": "puede donar a: A+,A-,AB+,AB-, puede recibir de: A-,O-",
               "O-": "puede donar a: todos, puede recibir de: O-", "B-": "puede donar a: B+,B-,AB+,AB-, puede recibir de: B-,O-",
               "AB-": "puede donar a: AB+,AB-, puede recibir de: A-,O-,B-,AB-"}

inf = tipo_sangre[plt]

html = """<html>
<head>
  <title>Tarea, erick rivera valdez</title>
  <style>
    body {
      background-color: lightblue;
    }
    .contenedor {
      position: absolute;
      display: flex;
      flex-direction: column;
      width: 400px;
      text-align: center;
      margin: 40px;
      margin-top: 0px;
      left: 50%;
      top: 50%;
      border: 2px solid black;
      border-radius: 5px;
      transform: translate(-50%, -50%);
    }
    img {
      width: 80px;
      margin-left: 10px;
      border-radius: 5px;
    }
    h1 {
      background-color: white;
      height: 100%;
      border-radius: 5px;
      padding: 10px 5px;
    }

    span {
      font-size: 2em;
      border: 2px solid white;
      border-radius: 5px;
      padding: 10px 5px;
      margin: 10px;
    }
  </style>
</head>

<body>
  <div class="contenedor">
    <h1>Este es el resultado.</h1>
    <span>Fecha De Nacimiento: @fecha</span>
    <span>Zodiaco: @zodiaco <img src="@zodiaco.jpg" alt="img"></span>
    <span>Compartibilidad: @compartibilidad</span>

  </div>
</body>

</html>"""
html = html.replace('@fecha', (f"{dia}-{mes}-{año}"))
html = html.replace('@zodiaco', (zodiacales[mes]))
html = html.replace('@compartibilidad', (inf))

f = open(f'{zodiacales[mes]}.html', 'w')
f.write(html)
f.close()


print("\nSe ha generado su archivo con exito! En la ubicacion del ejecuble python")

print("\nePresione cualquier tecla para terminar...")

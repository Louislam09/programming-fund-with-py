

zodiacales = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (21, 19, 20, 20, 21, 20, 21, 22, 23, 22, 23, 22)


dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes: "))
año = int(input("introduce el año: "))

mes = mes -1

if dia > fechas[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print ("Tu signo es: ", zodiacales[mes])

plt = str(input("ingrese su tipo de sangre: "))
tipo_sangre={"A+":"puede donar a: A+,B+, puede recibir de: B+,B-,O+,O-", "O+":"puede donar a: A+,O+,B+,AB, puede recibir de: O+,O-", 
"B+":"puede donar a: B+,AB+, puede recibir de: B+,B-,O+,O-", "AB+":"puede donar a: AB+, puede recibir de: todos", "A-":"puede donar a: A+,A-,AB+,AB-, puede recibir de: A-,O-" ,
"O-":"puede donar a: todos, puede recibir de: O-", "B-":"puede donar a: B+,B-,AB+,AB-, puede recibir de: B-,O-",
"AB-":"puede donar a: AB+,AB-, puede recibir de: A-,O-,B-,AB-"}

inf = tipo_sangre[plt]
print(inf)

html = """ <html>
  <head>  
    <title>Tarea, erick rivera valdez</title>'
  </head>

  <body>
    <h3>Este es el resultado.</h3>
    dia: @dia <br>
    mes: @mes <br>
    año: @año <br>
    zodiaco: @zodiaco <br>
    tipo_de_sangre: @tipo_de_sangre <br>

   
  </body>

</html> """
html = html.replace('@dia',srt(dia))
html = html.replace('@mes',srt(mes))
html = html.replace('año',str(año))
html = html.replace('@zodiaco', (zodiaco))
html = html.replace('@tipo de sangre', (tipo_de_sangre))

f=open('erick.html','w')
f.write(html)
f.close()
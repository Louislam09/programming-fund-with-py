
# Programa que acepte nombre,apellido,telefono y direccion de una persona. genere un archivo html que contenga esta informacion en un formato bonito y elegante
nombre = str(input("Ingrese solo su Nombre: "))
apellido = str(input("Ingrese solo su Apellido: "))
telefono = int and str(input("Ingrese su numero de Telefono:"))
print("Ingrese su direccion en este formato...\n 'Nombre de su sector, numero de su calle y casa': ")
sector = str(input("Nombre de su sector: "))
calle = int and str(input("El nombre de su calle: "))
casa = int and str(input("El numero de su casa: "))
print("Su direccion completa es: ", sector, calle, casa)
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
    <span>Nombre: @nombre</span>
    <span>Apellido: @apellido</span>
    <span>Numero de Telefono: @telefono</span>
    <span>Su sector es: @sector</span>
    <span>Calle: @calle</span>
    <span>Casa:@casa</span>

  </div>
</body>

</html>"""
html = html.replace('@nombre', (nombre))
html = html.replace('@apellido', (apellido))
html = html.replace('@telefono', str(telefono))
html = html.replace('@sector', (sector))
html = html.replace('@calle', (calle))
html = html.replace('@casa', str(casa))

f = open(f'{nombre}.html', 'w')
f.write(html)
f.close()


print("Se ha generado su archivo con exito! En la ubicacion del ejecuble python")

print("Presione cualquier tecla para terminar...")

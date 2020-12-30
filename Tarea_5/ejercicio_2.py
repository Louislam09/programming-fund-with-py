import requests
import json
import os


url = "http://adamix.net/gastosrd/api.php?act=GetContribuyentes&rnc="

os.system('cls')

print("""
--------------------------------
PROGRAMA QUE ACEPTA UN RNC Y
MUESTRA EL NOMBRE DE LA EMPRESA
--------------------------------
""")

code = input("Ingrese RNC de la empresa: ")


try:
    response = requests.get(url + code, timeout=5)

    if response.json() != 0:
        data = response.json()
        print(f"""\n
------------------------------------------------------
                NOMBRE DE LA EMPRESA
------------------------------------------------------
{data["RGE_NOMBRE"]}
    """)
    else:
        print(f"""\n
    ------------------------------------------------------
                    LA EMPRESA NO EXISTE!
    ------------------------------------------------------
        """)

except requests.ConnectionError:
    print(f"""\n
    ------------------------------------------------------
                    NO TIENES CONEXION!
    ------------------------------------------------------
        """)


input("Prsione cualquier tecla para salir...")

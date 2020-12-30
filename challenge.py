# Matriculas: 2019-7725,2019-7733,2019-8790
# Nombre capitan: Luis Martinez matricula: 2019-7725
# Nombre: Denzel Medina Matricula: 2019-7733
# Nombre: Victor Nolaco Matricula: 2019-8790

import os
import webbrowser


objecto_1 = [
    "Diccionario de indegena a espanol",
    "Este libro no sirvira para traduccir el idioma",
    "https://lh3.googleusercontent.com/DSLXeoqX9nO2CB9mFk0HHb_wW-FU65tKE9Bx9G8Xbrf_Cb8189zHL-GAL4Nj6tz30U6w=s85"
]
objecto_2 = [
    "libro de medicina",
    "Este libro le servira para las enfermedades",
    "https://image.slidesharecdn.com/completoenfermeriaymedicinatradicional-120207202314-phpapp02/95/enfermeria-y-medicina-tradicional-1-728.jpg?cb=1328646600"

]
objecto_3 = [
    "pintola",
    "En caso de que tengamos que defendernos",
    "https://lh3.googleusercontent.com/proxy/KkI7JkkwxPPrKuTYmWwIs3QkFv5-v363cPshbae5l5aqEJY2DQNH33_Aq2Jx_yAQ5lshwSF9f7CNrM5ujw9La2R84REwuQLksl6BuW-0mV3xlKjkMxSVPiEiyZ1s"
]


def show_obj(obj):
    os.system('cls')
    print("Objectos")
    print(f"""
    Nombre: {obj[0]}
    Descripcioni:{obj[1]}
    """)
    print("Presion cualquier teclas para ver la imagen")
    input()
    webbrowser.open_new_tab(obj[2])
    print("Presion cualquier teclas Para ver el siguiente")
    input()
    return


def start_program():
    show_obj(objecto_1)
    show_obj(objecto_2)
    show_obj(objecto_3)

    input("PRESIONE CUALQUIER TECLA PARA SALIR")


start_program()

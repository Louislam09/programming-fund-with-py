from os import system
import os
import pandas as pd
import matplotlib.pyplot as plf
import time
import webbrowser as wb

TITLE = "STUDEN'S AVERAGE"
link_video = 'index.html'

STUDENTS_DATA = []
AVERAGES = []
workbook = 'students_averages.xlsx'

def ask_data(txt):
    global content
    content  = input(txt)

    if len(content) == 0:
        ask_data(txt)
    else: 
        return content

def get_average(data):
    AVERAGES = []
    for student in data:
        student_info = f"{student[0]}({student[1]})"
        student_average = (student[2] +  student[3] +  student[4] +  student[5]) / 4

        AVERAGES.append([student_info,student_average])

    dataFrame = pd.DataFrame(AVERAGES,columns=['Nombre','Promedio'])
    dataFrame.to_excel(workbook)

def add_student():
    system('cls')
    print('Solicitad datos del estudiante')

    name = ask_data('Escribe el Nombre: ')
    enrollment = int(ask_data('Escribe la matricula: '))
    note1 = int(ask_data('Escribe la nota 1: '))
    note2 = int(ask_data('Escribe el nota 2: '))
    note3 = int(ask_data('Escribe el nota 3: '))
    note4 = int(ask_data('Escribe el nota 4: '))

    STUDENTS_DATA.append([name,enrollment,note1,note3,note3,note4])
    get_average(STUDENTS_DATA)


    print('presione cualquier tecla para volver al menu...')
    input()
    Menu()

def show_graph():
    system('cls')
    print('Grafica')

    if os.path.isfile(workbook):
        dataFrame = pd.read_excel(workbook)

        values = dataFrame[['Nombre','Promedio']]

        ax = values.plot.bar(x='Nombre',y='Promedio',rot=0)

        plf.show()
    else:
        print('No hay datos para mostrar!\n')

    print('presione cualquier tecla para volver al menu...')
    input()
    Menu()

def Menu():
    system('cls')
    print(TITLE)
    print("""
    1-AÑADIR DATOS DEL ESTUDIANTE
    2-MOSTRAR GRAFICA
    3-MOSTRAR VIDEO DE COMO HACER EL VIDEO
    4-SALIR
    """)

    option = input('Escribe tu opcion: ')
    options = ['1','2','3']

    if option in options:
        if option == '1':
            add_student()
        elif option == '2':
            show_graph()
        elif option == '3':
            wb.open(link_video)
        elif option == '4':
            return
    else:
        print('Escriba una opcion valida')
        time.sleep(2)
        Menu()



Menu()

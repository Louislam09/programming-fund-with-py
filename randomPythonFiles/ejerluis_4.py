def verificar():
    num1 = input('Digite el primer numero: ')
    num2 = input('Digite el segundo numero: ')
    cam_num1 = len(num1)
    cam_num2 = len(num2)

    ult_dig1 = int(num1[cam_num1 - 1])
    ult_dig2 = int(num2[cam_num2 - 1])
    
    if ult_dig1 == ult_dig2:
        print('los ultimos digitos son iguales', ult_dig1,'y',ult_dig2)

    else :
        print('los ultimos digitos son diferentes', ult_dig1,'y',ult_dig2 )     

    resp = input('Desea provar otra vez? ')

    if resp == 'si' or resp == 'Si':
        verificar()

    elif resp == 'no' or resp == 'No':
        input('Tu programa se cerrara!....\n Solo precione una tecla')    

verificar()

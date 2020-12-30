num = input('Digite un numero con mas de un digito: ')

res = input('Si los quieres ascendente presione (1) o descendente presione (2): ')
asc = sorted(num)
if res == '1':
    print(asc) 

elif res == '2':
    ad = list(asc)
    des = ad.reverse()
    print(ad)

input('Presione una tecla para cerrar')

 
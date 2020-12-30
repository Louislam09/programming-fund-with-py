# num = input("Digite un numero con mas de un digito: ")

# res = input("Si los quieres ascendente presione (1) o descendente presione (2): ")
# asc = sorted(num)
# if res == "1":
#     print(asc)

# elif res == "2":
#     ad = list(asc)
#     des = ad.reverse()
#     print(ad)

# input("Presione una tecla para cerrar")

num = input("Escribe un numero: ")
print("Ordenar:\n1)Ascendiente\n2)Descendiente")
res = input("Respuesta: ")


def order(num, res):
    if res == "1":
        n = list(num)
        n.sort()
        men = ""
        men = men.join(n)
        return men
    else:
        n = list(num)
        n.sort(reverse=True)
        may = ""
        may = may.join(n)
        return may


print(order(num, res))
input("Presione una tecla para cerrar")


# palabras = ["hola", "suriel", "!"]  # list
# unir = " "  # string
# unida = unir.join(palabras)
# print(unida)
# input()
# Eso presenta
# 123


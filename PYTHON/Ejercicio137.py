def get_int(mensaje):
    try:
        return int(input(mensaje))
    except:
        print('Este programa solo funciona con números!!')
        exit(1)


def cargar():
    lista = []
    for x in range(10):
        valor = get_int("Ingrese valor:")
        lista.append(valor)
    return lista


def generar_listas(lista):
    listanega = []
    listaposi = []
    for x in range(len(lista)):
        if lista[x]<0:
            listanega.append(lista[x])
        else:
            if lista[x]>0:
                listaposi.append(lista[x])
    return [listanega, listaposi]


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])

lista = cargar()
listanega, listaposi = generar_listas(lista)
print("Lista con los valores negativos")
imprimir(listanega)
print("Lista con los valores positivos")
imprimir(listaposi)

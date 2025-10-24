def get_float(mensaje):
    try:
        return float(input(mensaje))
    except:
        print('Este programa solo funciona con números!!')
        exit(1)

def carga_lista():
    li = []
    for x in range(5):
        valor = get_float("Ingrese valor: ")
        li.append(valor)
    return li

def retornar_mayormenor(li):
    ma = li[0]
    me = li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma = li[x]
        else:
            if li[x]<me:
                me = li[x]
    return [ma,me]

rango = retornar_mayormenor(carga_lista())
print("Mayor elemento de la lista: ", rango[0])
print("Menor elemento de la lista: ", rango[1])
print("Media de la lista: ", sum(rango) / len(rango))

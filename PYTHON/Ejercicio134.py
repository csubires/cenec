def get_int(mensaje):
    try:
        return int(input(mensaje))
    except:
        print('Este programa solo funciona con números!!')
        exit(1)

def cargar_datos():
    nom = []
    ed = []
    for x in range(5):
        nom.append(input("Ingrese el nombre de la persona:"))
        ed.append(get_int("Ingrese la edad: "))
    return [nom, ed]

def mayores_edad(nom, ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):
        if ed[x] >= 18:
            print(nom[x])

def promedio_edades(ed):
    suma = 0
    for x in range(len(ed)):
        suma = suma+ed[x]
    promedio = suma//5
    print("Edad promedio de las personas:", promedio)

nombres, edades = cargar_datos()
mayores_edad(nombres, edades)
promedio_edades(edades)

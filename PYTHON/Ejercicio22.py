# Ejercicio 82

nombres = []
for x in range(5):
    nom=str(input("Ingrese nombre de persona: "))
    nombres.append(nom)

    nombremenor = nombres[0]
    for x in nombres:
        if x < nombremenor:
            nombremenor = x

print("\nLa lista completa de nombres ingresado son", nombres)
print("El nombre menor en orden alfabetico es:", nombremenor)



# Ejercicio 83

lista3 = []
for x in range(5):
    valor = int(input('Ingrese valor: '))
    lista3.append(valor)

mayor = lista3[0]
for x in lista3:
    if x > mayor:
        mayor = x

print('Lista completa', lista3)
print('Mayor de la lista', mayor)

cantidad = 0
for x in lista3:
    if x == mayor:
        cantidad += 1
if cantidad > 1:
    print('El mayor se repite en la lista')

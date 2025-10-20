
lista1=[10, 5, 3]
lista2=[1.78, 2.65, 1.55, 89, 4]
lista3=['lunes', 'martes', 'miercoles']
lista4=['juan', 45, 1.34]

print(lista1)

for lista in lista3:
	print(lista)



lista5 = ['Madrid', 'Málaga', 'Sevilla', 'Toledo', 'Barcelona']
for x in lista5:
	print(x)


c = 0
suma = 0
while c < len(lista1):
    suma += lista1[c]
    c += 1

print("Resultado: ", suma)

suma = 0
for x in lista1:
    suma += x

print('Resultado: ', suma)
print('Un elemento', lista1[1])

print('Madriz' in lista5)
print('Madrid' in lista5)


for x in lista5:
    if x == 'Madrid':
        print("ENCONTRADO!!!")
        break
else:
    print("NO ENCONTRADO!!")

ciudades = ['Malaga', 'Sevilla', 'Cordoba', 'Jaen', 'Granada', 'Cadiz', 'Almeria']

ciudad = str(input("Dime el nombre de una ciudad: "))

for x in ciudades:
    if ciudad == x:
        print('Ciudad encontrada!!!')
        break
else:
    print('Ciudad NOOO disponible')





lista = ['ana', 7, 9]

print(f'Nombre del alumno: ', lista[0], 
        ', Promedio de sus notas: ', lista[1] + lista[2] // 2)


lista = [100, 23432, 324, 234 ,234, 234]
cantidad = 0

for list in lista:
    if list > 500:
        cantidad += 1

print('La lista está constituida por los elementos: ', lista)
print('Mayores de 500 ', cantidad)


# Ejercicio propuesto 73
lista11=[8, 1, 9, 2, 10]
x=0
print("Elementos de la lista con valores iguales o superiores a 7")
for x in lista11:
    if x >= 7:
        print(x)


# Ejercicio propuesto 74
nombres=["juan", "ana", "marcos", "carlos", "luis"]
cantidad=0
for elemento in nombres:
    if len(elemento)>=5:
        cantidad += 1
print("Todos los nombres son", nombres)
print("Cantidad de nombres con 5 o mas caracteres", cantidad)





#frutas = ['manzana', 'platano', 'uva', 'pera', 'naranja']
['manzana', 'platano', 'uva', 'pera', 'naranja']

if str(input('Dime el nombre de una fruta: ')) in ['manzana', 'platano', 'uva',
'pera', 'naranja']:
    print('Tu fruta está en la lista')
else:
    print('Tu fruta no está disponible')

# --------------------------

lista = []
for x in range(5):
    lista.append(int(input('Dime un valor:')))

print('El mayor valor introducido es:', max(lista))

# -------------------------- Ejercicio 81

lista2 = []
for x in range(5):
    lista2.append(int(input('Ingrese el valor: ')))

menor = min(lista2)
mayor = max(lista2)
posicion = lista2.index(menor)

print('Lista: ', lista2)
print(f'Menor {menor} en posicion {posicion}')
print('Mayor', mayor)






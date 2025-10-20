
def get_float(mensaje):
	try:
		return float(input(mensaje))
	except:
		print('Este programa solo funciona con números!!')
		exit(1)

x = 0
suma = 0
n = get_float('Cuantas personas hay: ')
while x < int(n):
    suma += get_float(f'Introduce Altura de la persona {x + 1}: ')
    x += 1

print('La altura promedio es ', round(suma / n, 2))

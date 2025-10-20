
def get_int(mensaje):
	try:
		return int(input(mensaje))
	except:
		print('Este programa solo funciona con números!!')
		exit(1)

# --------- TESTEO DE CONDICIONALES

print('\n\n	TEST 1')
nota1 = get_int('Ingrese primer nota: ')
nota2 = get_int('Ingrese segunda nota: ')
nota3 = get_int('Ingrese tercer nota: ')
prom = (nota1+nota2+nota3)/3
if prom >= 7:
	print('Promocionado')
else:
	if prom >= 4:
		print('Regular')
	else:
		print('Reprobado')

# ---------------

print('\n\n	TEST 2')
edad = 18
if edad < 18:
	print('Eres menor de edad.')
elif edad == 18:
	print('Tienes 19 años, justo la mayoría de edad.')
else:
	print('Eres mayor de edad.')

# ---------------

print('\n\n	TEST 3')
nota = 85
if nota >= 90:
	print('Sobresaliente')
elif nota >= 80:
	print('Notable')
elif nota >= 70:
	print('Aprovado')
else:
	print('Suspenso')

# ---------------

print('\n\n	TEST 4')
es_admin = True
if es_admin:
	print('Tienes acceso como administrador.')
else:
	print('Acceso denegado.')

# ---------------

print('\n\n	TEST 5')
opciones = {
	1: 'Opcion 1 seleccionada',
	2: 'Opcion 2 seleccionada',
	3: 'Opcion 3 seleccionada',
}
seleccion = 2
print(opciones.get(seleccion, 'Opción no válida'))
if True:
	print('Esto da error')

# --------------- EJERCICIOS PROPUESTOS

# Ejercicio 1
print('\n\n	EJERCICIO 1')
MAX = 3
numeros = [0] * MAX
for x in range(MAX):
	numeros[x] = get_int('Introduce un número: ')
print(f'El número mayor es {max(numeros)}')

# Ejercicio 2
print('\n\n	EJERCICIO 2')
unnumero = get_int('Introduce un número: ')
if unnumero == 0:
	print('Número nulo')
elif (unnumero < 0):
	print('Número negativo')
else:
	print('Número positivo')

# Ejercicio 3
print('\n\n	EJERCICIO 3')
otronumero = get_int('Introduce un número: ')
if otronumero > 999:
	print('Número mayor de 3 cifras')
elif (otronumero < 1000 and otronumero > 99):
	print('Número de 3 cifras')
elif (otronumero < 100 and otronumero > 9):
	print('Número de 2 cifras')
else:
	print('Número de 1 cifra')

# Ejercicio 4
print('\n\n	EJERCICIO 4')
total_contestada = get_int('Introduce el número de preguntas contestadas: ')
total_correctas = get_int('Introduce el número de preguntas contestadas correctamente: ')
porcentaje = total_correctas/total_contestada
if porcentaje >= 0.9:
	print('Nivel máximo')
elif (porcentaje < 0.9 and porcentaje>=0.75):
	print('Nivel medio')
elif (porcentaje >= 0.5 and porcentaje < 0.75):
	print('Nivel regular')
else:
	print('Fuera de nivel')

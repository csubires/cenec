
def get_int(mensaje):
	try:
		return int(input(mensaje))
	except:
		print('Este programa solo funciona con números!!')
		exit(1)

maximo = get_int('¿Cuantos número de fibonacci quieres? ')
anterior = 0
actual = 1
acumulador = 0
x = 0

print('\nACUMULADOR \t ANTERIOR \t ACUMULADOR')
while x < maximo:
    print(f'{acumulador} \t + \t {actual} \t = \t {actual + anterior}')
    acumulador = actual + anterior
    actual = anterior
    anterior = acumulador
    x += 1

print(f'\nNúmero final: \t\t\t {acumulador}')

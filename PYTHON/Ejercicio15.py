
def get_int(mensaje):
	try:
		return int(input(mensaje))
	except:
		print('Este programa solo funciona con números!!')
		exit(1)

x = 1
conta1 = 0
conta2 = 0
gastos = 0
n = get_int('Cuantos empleados tiene la empresa: ')
print()
while x <= n:
	sueldo = get_int(f'Ingrese el sueldo del empleado {x}: ')
	if sueldo <= 300:
		conta1 += 1
	else:
		conta2 += 1
	gastos += sueldo
	x += 1
print("\nCatidad de empleados con sueldos entre 100 y 300 : ", conta1)
print("Catidad de empleados con sueldos mayor a 300     : ", conta2)
print("Gasto total de la empresa en sueldos             : ", gastos)

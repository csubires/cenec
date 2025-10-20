

option = 2

match option:
	case 1:
		print('Has elegido la opción 1')
	case 2:
		print('Has elegido la opción 2')
	case 3:
		print('Has elegido la opción 3')
	case _:
		print('Opción no válida')


# EJERCICIO 1

def get_int(mensaje):
	try:
		return int(input(mensaje))
	except:
		print('Este programa solo funciona con números!!')
		exit(1)

match get_int('Introduce día de la semana: '):
	case 1:
		print('Hoy es LUNES')
	case 2:
		print('Hoy es MARTES')
	case 3:
		print('Hoy es MIERCOLES')
	case 4:
			print('Hoy es JUEVES')
	case 5:
			print('Hoy es VIERNES')
	case 6:
			print('Hoy es SABADO')
	case 7:
			print('Hoy es DOMINGO')
	case _:
		print('Opción no válida')

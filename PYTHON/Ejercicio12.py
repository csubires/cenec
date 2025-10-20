
contador = 1
num_alumnos = 5

aprobados = 0
suspensos = 0

while (contador <= num_alumnos):
	nota = int(input(f'Introduce la nota del alumno {contador}: '))
	if nota >= 5:
		aprobados += 1
	else:
		suspensos += 1
	contador += 1

print(f'Número de aprobados: {aprobados}')
print(f'Número de suspensos: {suspensos}')

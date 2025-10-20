MAYOR_EDAD=18
NOTA_APROBADO=5

try:
	edad=int(input('Ingrese edad: '))
	nota=float(input('Ingrese nota: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)

print(f'{"\nEnhorabuena! eres mayor de edad" if edad>=MAYOR_EDAD else "Prohibido menores!!"}')
print(f'{"Enhorabuena! has aprobado" if nota>=NOTA_APROBADO else "Suspensooo!!"}')

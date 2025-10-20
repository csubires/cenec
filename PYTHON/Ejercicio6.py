
MAYOR_EDAD=18
NOTA_APROBADO=5

try:
	edad=int(input('Ingrese edad: '))
	nota=float(input('Ingrese nota: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)

if (edad > 67):
	print('Enhorabuena! tas jubilaoh')
elif (edad < 67 and edad >=18):
	print('A tu edad ya tenía 3 pisos y 8 hijos!')
else:
	print('Nenucoo!!')

if (nota > 6 and nota <=10):
	print('Enhorabuena! has aprobado')
elif (nota < 6 and nota >=5):
	print('Ufff, aprovado por los pelos')
elif (nota > 10):
	print('Sos tremendo juaker, estas reprobado!!')
else:
	print('Suspensooo!!')


MAX=4
valores=[0]*MAX

try:
	for x in range(MAX):
		valores[x]=int(input(f'Ingrese el {x+1} valor: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)

suma=sum(valores)
promedio=suma/4
print(f'\nLa suma de los cuatro valores es, {suma}')
print(f'La promedio de los cuatro valores es, {promedio}')

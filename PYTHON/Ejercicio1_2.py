try:
	num1=int(input('Ingrese primer valor: '))
	num2=int(input('Ingrese segundo valor: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
print(f'La suma de los dos valores es {suma}')
print()
print(f'La resta de los dos valores es {resta}')
print()
print(f'La multiplicación de los dos valores es {multiplicacion}')
print()
try:
	division=num1/num2
	print(f'La división de los dos valores es {division}')
except Exception as e:
	print('Error: ', e);

try:
	num1=int(input('Ingrese primer valor: '))
	num2=int(input('Ingrese segundo valor: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)
print(f'El valor mayor es {num1 if num1>num2 else num2}')

#print("asaddasdasd", end=" ")
#print(345);

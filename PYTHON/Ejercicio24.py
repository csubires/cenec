def resta(numero1, numero2):
	print('la resta es', numero1 - numero2)

def suma(numero1, numero2):
	print('la suma es', numero1 + numero2)

def multi(numero1, numero2):
	print('la multiplicación es', numero1 * numero2)

def div(numero1, numero2):
	print('la división es', numero1 // numero2)

numero1= int(input('En verdad dime el operador 1; '))
numero2 = int(input('En verdad dime el operador 2; '))

suma(numero1, numero2)
resta(numero1, numero2)
multi(numero1, numero2)
div(numero1, numero2)

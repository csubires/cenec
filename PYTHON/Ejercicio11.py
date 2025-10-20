
x = 0
while x < 15:
	print(x, end=', ')
	x += 1
print()

# --------------------

x = 0
y = 2
while x < 11:
	print(f'{y} x {x} = {x*y}')
	x += 1 # x = x + 1

# --------------------

suma = 0
x = 0
num = 5
while x <= num:
    valor = int(input('Introduce valor: '))
    suma += valor
    x += 1

print(f'Suma total : {suma}')
print(f'Media      : {suma/num}')

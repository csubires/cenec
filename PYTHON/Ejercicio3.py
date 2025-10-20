
IVA=0.21
DESCUENTO=0.1

try:
	unidades=int(input('Ingrese las cantidad: '))
	importe=float(input('Ingrese el valor del importe: '))
except:
	print('Este programa solo funciona con números!!')
	exit(1)

base_imponible=importe*unidades
total=base_imponible-(base_imponible*DESCUENTO)
print('\n┌────────────────────┐\n│')
print('│   MERCADONA, S.A.\n│')
print(f'│ Importe     {(base_imponible):.2f}')
print(f'│ Descuento   {(base_imponible*DESCUENTO):.2f}')
print(f'│ IVA         {(total*IVA):.2f}\n│')
print(f'│ TOTAL (€)   {total+(total*IVA):.2f}\n│')
print('│ -------------------')
print(f'│ IVA       {IVA*100}%')
print(f'│ DESCUENTO {DESCUENTO*100}%')
print('└────────────────────┘')


""" Ejemplo:
Ingrese las cantidad: 5
Ingrese el valor del importe: 10

Total: 54.45€

base_imponible				-> 5 * 10 = 50
descuento					-> 50 * 0.1 = 5.0
base_imponible - descuento	-> 45
base_imponible + iva		-> 45 + (45*0.21 = 9.45)

TOTAL						-> 45 + 9.45 = 54.45
"""

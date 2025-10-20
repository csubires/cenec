x = 1
pares = 0
impares = 0
n= int(input("Cuantos número ingresará: "))

while x <= n:
    valor = int(input("Ingrese el valor: "))
    if valor %2 == 0:
        pares += 1
    else:
        impares+=1
    x+=1

print("Cantidad de pares ", pares)
print("Cantidad de impares", impares)



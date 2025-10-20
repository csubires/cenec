x = 1
suma1 = 0
suma2 = 0

print("primer lista")
while x <= 5:
    valor=int(input("Ingrese valor:"))
    suma1=suma1+valor
    x+=1



print("Segunda lista")
x = 1
while x <= 5:
    valor=int(input("Ingrese valor:"))
    suma2=suma2+valor
    x+=1


if suma1>suma2:
    print("Lista 1 mayor.")
else:
    if suma2>suma1:
        print("Lista2 mayor.")
    else:
        print("Listas iguales.")


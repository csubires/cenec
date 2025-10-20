



x = 1
n = int(input("Número personas: "))

mayor = 0
menor = 0

for x in range(n):
    edad = int(input("Introduce edad: "))

    if edad >= 18:
        mayor += 1
    else:
        menor += 1

print("Mayores de edad: ", mayor)
print("Menores de edad: ", menor)


def sumar(v1, v2, v3=0, v4=0, v5=5):
    s = v1 + v2 + v3 + v4 + v5
    return s


print("La suma de 5 + 6", sumar(5, 6))
print("La suma de 1 + 2 + 3", sumar(1, 2, 3))
print("La suma de 1 + 2 + 3 + 4 + 5", sumar(1, 2, 3, 4, 5))
x = sumar(1, 2, 3, 4, 5)
print(x)

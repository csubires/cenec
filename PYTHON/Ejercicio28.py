
def get_float(mensaje):
    try:
        return float(input(mensaje))
    except:
        print('Este programa solo funciona con números!!')
        exit(1)


def retornar_mayor(v1,v2):
    return v1>v2 and v1 or v2

print(retornar_mayor(
                    get_float("Ingrese el primer valor: "),
                    get_float("Ingrese el segundo valor: ")
                ))

# Otro ejercicio ------------------------

def inmc(peso, altura):
    mc = peso / (altura ** 2)
    return mc

peso = get_float('Ingrese su peso: ')
altura = get_float('Ingrese altura: ')

print('Su mmc es', inmc(peso, altura))

# -------------------------

def dame_nota(nota):
    return 'Estas aprobado' if nota >= 5 else 'Estas suspenso'

print(dame_nota(get_float('Inserte tu nota de examen: ')))

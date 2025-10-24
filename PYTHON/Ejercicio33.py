

PRECIO_BASE = 400

class Seguro:

    def __init__(self, modelo, kilometro, matriculacion):
        self.modelo = modelo
        self.kilometro = kilometro
        self.matriculacion = matriculacion

    def imprimir(self):
        print(f'Coche {self.modelo} de {self.matriculacion}, con {self.kilometro} kms.\t', end='')


    def pagarseguro(self):
        if self.matriculacion < 2010:
            print('Total a pagar: ', PRECIO_BASE + PRECIO_BASE * 0.1)
        else:
            print('Total a pagar: ', PRECIO_BASE + PRECIO_BASE * 0.05)


coche1 = Seguro('Ford focus', 344000, 2010)
coche1.imprimir()
coche1.pagarseguro()

coche2 = Seguro('Seat Ibiza', 66200, 2020)
coche2.imprimir()
coche2.pagarseguro()

coche3 = Seguro('Citroen C5', 2344000, 1970)
coche3.imprimir()
coche3.pagarseguro()

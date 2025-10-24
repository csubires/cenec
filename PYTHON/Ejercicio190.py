
IMPUESTOS = 0.21


class Empleado:

    def __init__(self):
        self.nombre = input('Ingrese el nombre del empleado: ')
        self.apellido = input('Ingrese el apellido del empleado: ')
        self.sueldo = float(input('Ingrese el sueldo: '))

    def imprimir(self):
        print('Nombre:',self.nombre)
        print('Apellido:',self.apellido)
        print('Sueldo:',self.sueldo)


    def calcular_impuesto(self):
        return self.sueldo * IMPUESTOS

    def paga_impuestos(self):
        if self.sueldo > 3000:
            self.sueldo += self.calcular_impuesto()
            print(f'Debe pagar impuestos. Sueldo final: {self.sueldo} €, Para hacienda: {self.calcular_impuesto()} €')
        else:
            print('No paga impuestos')


empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

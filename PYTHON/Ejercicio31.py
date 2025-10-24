

class Calculadora:

    def __init__(self):
        self.numero1 = int(input('Introduce numero1: '))
        self.numero2 = int(input('Introduce numero2: '))
        self.result = 0

    def suma(self):
        print('Operacion:', 'suma')
        self.result = (self.numero1 + self.numero2)


    def resta(self):
        print('Operacion:', 'resta')
        self.result = (self.numero1 - self.numero2)


    def multi(self):
        print('Operacion:', 'multiplicación')
        self.result = (self.numero1 * self.numero2)


    def div(self):
        print('Operacion:', 'división')
        self.result = (self.numero1 // self.numero2)

    def resultado(self):
        print('El resultado es:', self.result)


calculo = Calculadora()
calculo.suma()
calculo.resultado()
calculo.resta()
calculo.resultado()
calculo.multi()
calculo.resultado()
calculo.div()
calculo.resultado()

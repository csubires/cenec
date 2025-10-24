class Coche:

    def inicializar(self, motor, ruedas, tipo):
        self.motor = motor
        self.ruedas = ruedas
        self.tipo = tipo

    def arrancar(self):
        print(f'El coche {self.tipo} arranca')

    def acelerar(self):
        print(f'El coche acelera con {self.motor}')

    def frenar(self):
        print(f'El coche frena con {self.ruedas} ruedas')


coche1 = Coche()
coche1.inicializar('30 caballos', 4, 'flagoneta')
coche1.arrancar()
coche1.acelerar()
coche1.frenar()

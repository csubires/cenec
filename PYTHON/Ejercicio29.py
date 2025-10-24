class Gato:

    def inicializar(self, duenio):
        self.duenio = duenio

    def miau(self):
        print('Mi gato', self.duenio, 'Maulla')

    def comer(self):
        print('Mi gato', self.duenio, 'come atún')




gato1 = Gato()
gato1.inicializar('diego')
gato1.comer()
gato1.miau()


class Persona:

    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print('Nombre', self.nombre)
        print('Edad', self.edad)

    def mayor_edad(self):
        if self.edad >= 18:
            print('Es mayor de edad')
        else:
            print('No es mayor de edad')




persona1 = Persona()
persona1.inicializar('diego', 40)
persona1.imprimir()
persona1.mayor_edad()


class Persona3:

    def inicializar(self, nombre, edad, direccion, codigo_postal, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.telefono = telefono

    def imprimir(self):
        print('Nombre', self.nombre)
        print('Edad', self.edad)
        print('direccion', self.direccion)
        print('codigo_postal', self.codigo_postal)
        print('telefono', self.telefono)

    def mayor_edad(self):
        if self.edad >= 18:
            print('Es mayor de edad')
        else:
            print('No es mayor de edad')




persona31 = Persona3()
persona31.inicializar('pedrooo', 43, 'calle alcaparra', 29700, 66344233)
persona31.imprimir()
persona31.mayor_edad()

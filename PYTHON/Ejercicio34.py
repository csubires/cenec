
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def imprimir_producto(self):
        print(f'ID Producto: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}€')


class Fabricante:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def imprimir_fabricante(self):
        print(f'Fabricante: {self.nombre}, País: {self.pais}')

class Movil(Producto, Fabricante):

    def __init__(self, id, nombre, precio, fabricante_nombre, fabricante_pais, ram, almacenamiento):
        Producto.__init__(self, id, nombre, precio)
        Fabricante.__init__(self, fabricante_nombre, fabricante_pais)
        self.ram = ram
        self.almacenamiento = almacenamiento

    def imprimir_ticket(self):
        self.imprimir_fabricante()
        self.imprimir_producto()
        print(f'RAM: {self.ram}GB, Almacenamiento: {self.almacenamiento}GB')



movil1 = Movil(34, 'Galaxi', 3444, 'Sansung', 'Korea', 8, 256)
movil1.imprimir_ticket()

print("\n" + "="*50 + "\n")

movil2 = Movil(45, 'iPhone', 999, 'Apple', 'USA', 6, 128)
movil2.imprimir_ticket()

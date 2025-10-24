
class Alumno:

    def __init__(self, nombre, asignatura, nota):
        self.nombre = nombre
        self.asignatura = asignatura
        self.nota = nota

    def imprimir(self):
        print('\nnombre:', self.nombre, 'asignatura:', self.asignatura, 'nota:', self.nota)

    def calificar(self):
        print(f'El alumno {self.nombre} en la asignatura {self.asignatura} está {"Aprobado" if self.nota >=5 else "Suspenso"}')
        print('___________________________________________________')


alumno1 = Alumno('Pepito', 'Matemática', 5)
alumno1.imprimir()
alumno1.calificar()

alumno1 = Alumno('Maria', 'Matemática', 15)
alumno1.imprimir()
alumno1.calificar()

alumno1 = Alumno('Sergio', 'Ingles', 4)
alumno1.imprimir()
alumno1.calificar()

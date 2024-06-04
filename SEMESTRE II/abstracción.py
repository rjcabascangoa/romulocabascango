class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("lADRA")

class Gato(Animal):
    def hacer_sonido(self):
        print("MAULLA")

perro = Perro("FIRU", 5)
gato = Gato("CASCABEL", 6)

perro.hacer_sonido()
gato.hacer_sonido()

#(Las clases Perro y Gato heredan de la clase Animal y proporcionan su propia implementación del método hacer_sonido,

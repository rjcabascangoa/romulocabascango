class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("El vehículo está acelerando")

class Coche(Auto):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def abrir_puertas(self):
        print("Se abren Puetas del carro")

coche = Coche("Toyoya", "Prius", "Verde")
print(coche.marca)
coche.acelerar()
coche.abrir_puertas()

#(  La Auto Coche hereda de la clase Vehiculo, lo que le permite adquirir los atributos y métodos de la clase padre,
# y además define  Se abren Puetas del carro)


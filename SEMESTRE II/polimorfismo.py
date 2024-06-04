class Figurageometrica:
    def calcular_de_area(self):
        pass

class Rectangulo(Figurageometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_de_area(self):
        return self.base * self.altura

class Circulo(Figurageometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_de_area(self):
        return 3.14159 * self.radio**2

rectangulo = Rectangulo(55, 3)
circulo = Circulo(2)

print(rectangulo.calcular_area())  # Output: 15
print(circulo.calcular_area())  # Output: 12.56636

#( Tanto Rectangulo como Circulo son clases que heredan de Figura y ambas implementan su propio método calcular_area(),
# permitiendo tratarlas de manera uniforme a pesar de que su comportamiento varía según el tipo de figura).


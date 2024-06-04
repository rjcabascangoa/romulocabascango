class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
# Uso de la clase
persona = Persona("KATTY", 37)
print(persona.get_nombre())
persona.set_nombre("JAVIER")
print(persona.get_nombre())

#(En este caso, los atributos _nombre y _edad se encuentran encapsulados y se accede a ellos mediante métodos get y set,



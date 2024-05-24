print('Ejercicio de Metodo 2')
class Calculadora:
    def __init__(self,n1,n2):
        self.suma=n1+n2
        self.resta=n1-n2
        self.division=n1/n2
        self.multiplicacion=n1*n2
operacion=Calculadora(1,2)
print(operacion.suma,operacion.resta,operacion.division,operacion.multiplicacion)
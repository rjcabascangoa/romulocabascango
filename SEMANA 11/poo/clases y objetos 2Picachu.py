class Picachu:
    tipo='electrico'
    def __init__(self,nombre,nivel,sal):
        self.nombre=nombre
        self.nivel=nivel
        self.sal=sal
picachu1=Picachu('LUNA',333,600)
picachu2=Picachu('pelusa',3323,60340)
print(picachu1.tipo,picachu1.nivel,picachu1.sal,picachu2.tipo,picachu1.nombre)
print(picachu2.nivel,picachu2.nivel,picachu2.sal,picachu2.tipo,picachu2.nombre)
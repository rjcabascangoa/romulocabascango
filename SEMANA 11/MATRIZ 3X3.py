matriz = [[5, 6, 4],
          [8, 9, 1],
          [3, 2, 7]]
print(matriz)
print(f" {matriz[0][0]} {matriz[0][1]}")
print(f" {matriz[1][0]} ")
print("Mostrar los elementos fila x fila")
for row in matriz: print(row)
print("Mostrar los elementos columnas x columna")
for row in matriz:
    for element in row: print(element)
print("Ingrese la cantidad de fila y columna deseadas")
rows = int(input("¿Cuantas filas tendrá la matriz?: "))
columns = int(input("¿Cuantas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)


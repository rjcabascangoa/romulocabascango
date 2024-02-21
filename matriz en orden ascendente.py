
print("Orden una matriz forma ascendente")
'''rows = int(input("¿Cuantas filas tendrá la matriz?: "))
columns = int(input("¿Cuantas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila {row_position}: ")))
    matrix.append(row)
    print(row)'''
matrix=[3,4,1,6,9,8,0,3,5,6]
print("Matriz de original",matrix)
band=False
while band==False:
      band=True
      for i in range(len(matrix)-1):
         if matrix[i]>matrix[i+1]:
            aux=matrix[i+1]
            matrix[i]=matrix[i+1]
            matrix[i+1]=aux
            band=False
            print("Matriz Ordenada: ",matrix)


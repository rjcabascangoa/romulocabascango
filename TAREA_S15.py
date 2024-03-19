print("Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves nombre, edad,  y profesio")
diccionario_personal={"Javier":{"EDAD : ":37,"PESO  :":80,"ESTATURA: ":1.67},"KATTY":{"EDAD : ":32,"PESO  :":90,"ESTATURA: ":1.40}}
print(diccionario_personal)
print(diccionario_personal["Javier"])
print(diccionario_personal["KATTY"])

diccionario_personal1={"Nombre: ":"DIANA","CUIDAD":"CAYAMBE","PROFECCION":"SECRETARIA"}
diccionario_personal1["PESO: "]="80 KG" #AGREGAR UN NUEVO ELEMENTO
diccionario_personal1["RELIGION: "]="CATOLICO" #AGREGAR UN NUEVO ELEMENTO
diccionario_personal1["RELIGION: "]="JUDIO"# SE MODIFICA
del diccionario_personal1["PESO: "]# SE ELIMINA UN ELEMENTO
print(diccionario_personal1)

print(diccionario_personal1["Nombre: "])
print(diccionario_personal1["CUIDAD"])
print(diccionario_personal1["PROFECCION"])
def temperatura_promedio(ciudad_temperatura):
    temperatura_promedio={}
    for ciudad, temperatura in ciudad_temperatura.items():
        promedio= sum(temperatura)/len(temperatura)
        temperatura_promedio[ciudad]=promedio
    return temperatura_promedio
ciudad_temperatura={
"Cayambe":[22,23,10,15,11],
"Ayora":[22,23,10,15,11],
"Quito":[21,22,11,16,13],
"Juan Montalvo":[22,23,19,11,12]
}
temperatura= temperatura_promedio(ciudad_temperatura)
print("Temperatura promedio por ciudades",temperatura)

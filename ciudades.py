#Crear programa que devuelva ciudades

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas= devuelve_ciudades("Madrid", "Medellin", "itagui", "Envigado")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
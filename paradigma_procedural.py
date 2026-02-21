## Usamos funciones para organizar el codigo

# PARADIGMA PROCEDURAL

def registrar_entrada(lista, placa):
    #agregar un vehiculo a la lista
    lista.append(placa)
    
def registrar_salida(lista, placa):
    #elimina vehiculo si existe
    if placa in lista:
        lista .remove(placa)

vehiculos= []

registrar_entrada(vehiculos,"AAA111")
registrar_entrada(vehiculos,"BBB222")


print("Vehiculos: ", vehiculos)

registrar_salida(vehiculos,"AAA111")

print("Después de salida: ", vehiculos)

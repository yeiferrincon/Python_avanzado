##paradigma funcional

##usamos funciones puras (sin cambiar datos originales)

#paradigma funcional

def calcular_total(horas):
    #no cambia nada externo
    return horas * 2000

total = calcular_total(3)
print("Total a pagar: ", total)
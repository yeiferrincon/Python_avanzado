##PARADIGMA DECLARATIVO
##Decimos que queremos, no como

#Paradigma delcarativo usamos compresion de listas

vehiculos = ["ABC123", "BBB222", "CCC333"]

#Queremos solo placas que empiezan por B
filtrado = [v for v in vehiculos if v.startswith("B")] ## esta funcion hace el filtrado por nosotros, no le decimos cómo hacerlo, solo qué queremos

print ("filtramos: ", filtrado)

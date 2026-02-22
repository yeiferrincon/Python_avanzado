## Ejercicio 2 - Herencia
#Una clase hereda de otra

# herencia

class vehiculo:
    def __init__(self, placa):
        self.placa = placa
    
    def info(self):
        print("Placa:", self.placa)
        
class Moto(vehiculo):
    def __init__(self, placa, casco):
        super().__init__(placa) ## Hereda placa
        self.casco = casco
        
    
    def info_moto(self):
        print("Placa: ", self.placa, "Casco: ", self.casco)

m= Moto("XXY999", True)
m.info()
m.info_moto()
        
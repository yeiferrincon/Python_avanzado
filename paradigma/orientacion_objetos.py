##PARADIGMA ORIENTADO A OBJETOS (OOP)

##Modelamos el mundo real

#Paradigma OOP

class vehiculo:
    #constructor
    def __init__(self, placa):
        self.placa = placa #Guardamos placa
        
    def mostrar(self):
        #Metodo para mostrar placa
        print ("Placa: ", self.placa)
        
#crear obejto
v1 = vehiculo("ABC123")
v1.mostrar()
##caracteristicas: objetos y classes

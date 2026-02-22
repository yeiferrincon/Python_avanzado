#ejemplo de la vida real

#piensa en el boton "pagar" en tu parqueadaro

#Cliente carro → paga 3000

#cliente moto → paga 6000

#el boton se llama igual: pagar
#pero hace cosas diferentes.

# Creamos clases diferentes

class Carro:
    def pagar(self):
        #este metodo es para carros
        print("Carro paga 3000")

class Moto:
    def pagar(self):
        #este metodo es para camiones
        print ("Moto paga 1500")

class Camion:
    def pagar(self):
        #este metodo es para camiones
        print("Camion paga 6000")
        
#funcion que usa cualquier objeto
def cobrar(vehiculo):
    #no sabemos si es carro, moto o camion
    #solo sabemos que tiene pagar()
    vehiculo.pagar()

#creamos los objetos
c = Carro()
m = Moto()
cam= Camion()

#usamos la misma funcion
cobrar(c)
cobrar(m)
cobrar(cam)
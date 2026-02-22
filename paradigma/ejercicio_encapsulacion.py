##ejercicio 1 - encapsulacion
##proteger datos dentro de una clase

#Encapsulación

class cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo # privado con __
        
    def ver_Saldo(self):
        #Médtodo para ver saldo
        print("saldo: ", self.__saldo)
        
    def pagar(self, valor):
        # modoficar solo de forma segura
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Pago realizado")
        else:
            print("Saldo insuficiente")
            
c = cliente("Andres", 50000)

c.ver_Saldo()
c.pagar(20000)
c.ver_Saldo()

#c.__saldo x ERROR porque es privado
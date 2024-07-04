#Importamos las clases
from mi_paquete.modulo1 import Cliente
from mi_paquete.modulo1 import Compra

#Creo los objetos "clientes+compra"
cliente1 = Cliente("Alan","Martin", 30, "alan123@gmail")
compra1 = Compra("Computadora", "PC Center")

cliente2 = Cliente("Pedro", "Farias", 40, "pedrito123@gmail")
compra2 = Compra("Auriculares", "Walmart")

print(f"Total de clientes registrados: {Cliente.cantidad}")

print(cliente1)
print(compra1)
cliente1.mail()

print(cliente2)
print(compra2)
cliente2.mail()
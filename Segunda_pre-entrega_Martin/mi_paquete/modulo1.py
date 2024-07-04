#Creamos una clase con el nombre "Cliente"
class Cliente():
    
    #Atributos de clase
    cantidad =0
    
    #Constructor
    def __init__(self, nombre, apellido, edad, correo):
        
        #Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        
        Cliente.cantidad += 1
        
    #Métodos
    def __str__(self):
        return (f"\nSe ha creado cliente: " +self.nombre+" "+self.apellido+"")
    
    def mail(self):
        print (f"Se ha enviado la factura de la compra al correo: {self.correo}")
    
#Creo otra clase para agregar atributos especiales al cliente
class Compra():
        def __init__(self, item, tienda):
            self.item = item
            self.tienda = tienda
            
        def __str__(self):
            return (f"Compra realizada: {self.item}\nTienda: {self.tienda}\n")
        
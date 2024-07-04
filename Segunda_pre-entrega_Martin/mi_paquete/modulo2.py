#Primera_pre-entrega_Martin

#creamos un diccionario vacío simulando una base de datos.
Usuarios_dict = {}

#función para registrar y generar nuevo usuario y contraseña.
def GenUsrPass (Usuarios_dict):
    Usuario = input("Crear un nuevo nombre de usuario: ")
    Contraseña = input("Crea una contraseña: ")
    if Usuario in Usuarios_dict:
        print("El nombre de usuario ya existe")
    elif len(Contraseña) <6:
        print("La contraseña debe tener al menos 6 caracteres")
    else:
        print("Usuario creado con éxito")

Usuario = "Alan"
Contraseña = "123456"

Usuarios_dict [Usuario] = Contraseña

GenUsrPass (Usuarios_dict)

#función para mostrar usuarios y contraseñas guardados.
def Mostrar (UsrPss):
    print("Usuarios y Contraseñas almacenadas:")
    print(UsrPss)
    Mostrar (Usuarios_dict)
    
#funcion para iniciar sesión (compara los datos introducidos con los datos almacenados)
def Login (Usuarios_dict):
    UsrLogin = input("Inicia sesión con tu nombre de usuario: ")
    UsrPass = input("Ingresa tu contraseña: ")

UsrLogin = Usuario
UsrPass = Contraseña

if Usuarios_dict:
    if UsrLogin in Usuarios_dict:
        if Usuarios_dict [UsrLogin] == UsrPass:
            print("Haz iniciado sesión correctamente")
    else:
        print("Nombre de usuario o contraseña incorrectos")
        
        Login (Usuarios_dict)
        
UsrLogin = Usuarios_dict

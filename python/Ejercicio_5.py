"""
Diseña un sistema de autenticación multinivel utilizando decoradores en Python. Debes implementar tres niveles 
de autenticación: usuario, administrador y superusuario. Cada nivel debe requerir credenciales específicas 
para acceder a ciertas funciones. Utiliza decoradores para verificar la autorización antes de permitir el 
acceso a las funciones correspondientes.

"""

#Informacion a utilizar
user_info = {
    'name': 'jesus',
    'role': 'admin',
    'session': True
}

def guard(function):
    def verify(*args, **kwargs):
        view= str(function).split(" ")[1] #Obtener el nombre de la vista donde se desea ingresar
        user= args[0] if args else kwargs #Guardar la informacion que se recibe

        if user["session"]:
            if view=="editUser" and user["role"] == "superUsuario":
                function(user)
            elif view=="updateCatalog" and user["role"]=="admin":
                function(user)    
            elif view=="home":
                function(user)  
            else:
                print("No tienes permisos para entrar a la vista: ", view)
        else:
            print("¡No pudo iniciar sesión!")
            loggin()
    return verify


def loggin(): #Cualquiera puede entrar al loggin
    print("Entró al loggin")

@guard
def home(user): #Todos los que se autentiquen, pueden entrar al home (Este fue hecho para usuarios)
    print("Entró al home")

@guard
def editUser(user): #Solo los superUsuario pueden entrar al aditUser y editar los usuarios
    print("Entró al editUser")

@guard
def updateCatalog(user): #Solo los admin pueden entrar al updateCatalog y actualizar los productos de la pagina
    print("Entró al updateCatalog")

#home(user_info)
#editUser(user_info)
updateCatalog(user_info)

#US1- Create register
users = []

def createUser():
    user = []
    id = int(input("Ingrese su documento de identidad"))
    user.append(id)
    user_name = input("Ingrese su nombre")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido")
    user.append(user_last_name) 
    phone = input("Ingrese su teléfono")
    user.append(phone)
    user_email = input("Ingrese su correo electrónico")
    user.append(user_email)
    user_password = input("Ingrese su correo contraseña")
    user.append(user_password)
    users.append(user)
    
createUser()
createUser()
createUser()

print(users)

    

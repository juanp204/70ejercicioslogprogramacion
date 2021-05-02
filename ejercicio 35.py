lista = {"pedro":"1234"}
nombre = input("usuario = ")
contraseña = input("contraseña = ")
try:
    if lista[nombre] == contraseña:
        print("aceptado")
    else:
        print("contraseña invalida")
except:
    print("no existe el nombre de usuario")

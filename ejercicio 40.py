print("solo numeros entre 1 y 7")
numeros = ["apocalipsis","lunes","martes","miercoles","juevez","viernes","sabado","domingo"]
while True:
    try:
        print(numeros[int(input("numero = "))])
        break
    except ValueError:
        print("solo numeros")
    except IndexError:
        print("no existe ese dia de la semana")


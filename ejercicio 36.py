print("solo numeros entre 0 y 10")
numeros = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
while True:
    try:
        print(numeros[int(input("numero = "))])
        break
    except ValueError:
        print("solo numeros")
    except IndexError:
        print("solo numeros entre 0 y 10")

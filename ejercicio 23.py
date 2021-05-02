while True:
    try:
        num = float (input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    if num<0:
        print("el numero es negativo")
    else:
        print("el numero es positivo")


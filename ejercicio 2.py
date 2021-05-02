while True:
    try:
        numero = int(input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    print("el cuadrado del numero",numero,"es",numero**2)
    break
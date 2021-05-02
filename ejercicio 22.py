while True:
    try:
        num = int(input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    if num%2 == 0:
        print("el numero es par")
    else:
        print("el numer es impar")



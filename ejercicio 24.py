while True:
    try:
        num = float(input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    if num<0 and num%2 == 0:
        print("el numero es negativo, y es par")
    elif num>0 and num%2 == 0:
        print("el numero es positivo y es par")
    elif num<0:
        print("el numero es negativo y es impar")
    else:
        print("el numero es positivo y es impar")
    break

while True:
    try:
        numero1 = int(input("numero1 ="))
        numero2 = int(input("numero2 = "))
    except ValueError:
        print("solo numeros")
        continue
    print("suma =",numero1+numero2)
    print("resta =",numero1-numero2)
    print("multiplicacion =",numero1*numero2)
    print("divicion =",numero1//numero2)
    print("residuo =",numero1%numero2)
    break


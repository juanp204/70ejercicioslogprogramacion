while True:
    try:
        numero1 = int(input("numero1 ="))
        numero2 = int(input("mas numero2 = "))
    except ValueError:
        print("solo numeros")
        continue
    print("la suma de",numero2,"+",numero1,"=",numero1+numero2)
    break



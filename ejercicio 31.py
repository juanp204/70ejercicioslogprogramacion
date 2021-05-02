while True:
    try:
        num1 = float(input("numero 1 = "))
        num2 = float(input("numero 2 = "))
        num3 = float(input("numero 3 = "))
        if num1+num2>num3:
            print("la suma del primero con el segundo es mayor que el tercero")
        else:
            print("la suma del primero con el seguno NO es mayor que el tercero")
        break
    except ValueError:
        print("solo numeros")
        continue


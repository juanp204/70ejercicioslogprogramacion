while True:
    try:
        num1 = int(input("num1 = "))
        num2 = int(input("num2 = "))
        num3 = int(input("num3 = "))
        if num1==num2 or num1==num3 or num2==num3:
            print("hay almenos dos numeros iguales")
        else:
            print("no hay ningun numero igual")
        break
    except ValueError:
        print("solo numeros")
        continue


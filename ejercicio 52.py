while True:
    try:
        n = int(input("numero = "))
        if n<0:
            print("es negativo")
            continue
        else:
            print(n)
            break
    except ValueError:
        print("solo numeros")
        continue


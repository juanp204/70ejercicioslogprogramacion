while True:
    try:
        num = (input("numero = "))
        int(num)
        if len(num) != 4:
            print("solo numero de 4 digitos")
            continue
    except ValueError:
        print("solo numeros")
        continue
    num = list(num)
    num.reverse()
    for x in range(len(num)):
        print(num[x], end="")
    break
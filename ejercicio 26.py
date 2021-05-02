while True:
    try:
        num = int(input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    if num>=10:
        print(num*3)
    else:
        print(num/4)


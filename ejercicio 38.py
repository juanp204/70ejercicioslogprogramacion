while True:
    try:
        num1 = int(input("num1 = "))
        num2 = int(input("num2 = "))
        num3 = int(input("num3 = "))
        if num1>num2>num3:
            print("esta decrementando")
        elif num1<num2<num3:
            print("esta incrementando")
        else:
            print("ni incrementa ni disminuye")
        break
    except ValueError:
        print("solo numeros")
        continue


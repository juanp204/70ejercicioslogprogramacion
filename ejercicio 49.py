promedio = 0
for x in range(1,11):
    while True:
        try:
            promedio += int(input("num"+str(x)+" = "))
            break
        except ValueError:
            print("solo numeros")
            continue
print("promdeio es igual a =",promedio/10)


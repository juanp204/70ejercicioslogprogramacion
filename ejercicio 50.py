promedio = []
try:
    for x in range(1,int(input("cuantos numeros = "))+1):
        while True:
            try:
                promedio.append(int(input("num"+str(x)+" = ")))
                break
            except ValueError:
                print("solo numeros")
                continue
except:
    print("solo numeros")
print("promdeio es igual a =",sum(promedio)/len(promedio))


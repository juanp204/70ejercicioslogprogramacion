numeros = []
for x in range(3):
    while True:
        try:
            numeros.append(int(input("numero"+str(x+1)+" = ")))
            break
        except:
            print("solo numeros")
            continue
print("el perimetro",sum(numeros)/3)



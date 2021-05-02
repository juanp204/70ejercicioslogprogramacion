print("no coloques anda para finalizar")
mayor100 = 0
menor100 = 0
while True:
    try:
        n = input("cuantos numeros = ")
        if not bool(n):
            break
        if int(n)>100:
            mayor100 += 1
        else:
            menor100 += 1
    except ValueError:
        print("solo numeros")
        continue
print("la cantidad de numeros mayores a 100 fueron",mayor100)
print("la cantidad de numeros menores a 100 fueron",menor100)
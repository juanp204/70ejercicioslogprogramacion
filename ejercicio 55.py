print("no coloques nada para finalizar")
numeros = 0
cinco = 0
pares = 0
impa = 0
while numeros<10 and cinco<20:
    try:
        n = input("num= ")
        if not int(n)%2:
            pares += 1
        else:
            impa += 1
        if int(n) == 5:
            cinco +=1
            print(cinco)
        else:
            numeros+=1
    except ValueError:
        print("solo numeros")
        continue
print("la cantidad de numeros digitados fue",numeros+cinco)
print("la cantidad de cincos digitados es",cinco)
print("la cantidad de numeros pares es",pares)
print("la cantidad de numeros impares es",impa)


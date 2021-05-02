print("no coloques nada para finalizar")
nump = 0
numn = 0
pares = 0
impa = 0
mlocho = 0
while True:
    try:
        n = input("cuantos numeros = ")
        if not bool(n):
            break
        if int(n)>0:
            nump += 1
        else:
            numn += 1
        if not int(n)%2:
            pares += 1
        else:
            impa += 1
        if not int(n)%8:
            mlocho += 1
    except ValueError:
        print("solo numeros")
        continue
print("la cantidad de numeros positivos es",nump)
print("la cantidad de numeros negativos es",numn)
print("la cantidad de numeros pares es",pares)
print("la cantidad de numeros impares es",impa)
print("la cantidad de numeros multiplos de 8 es",mlocho)


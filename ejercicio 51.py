promedioimpares= []
promediopares = []
try:
    for x in range(1,int(input("cuantos numeros = "))+1):
        while True:
            try:
                n = int(input("num"+str(x)+" = "))
                if n%2:
                    promedioimpares.append(n)
                else:
                    promediopares.append(n)
                break
            except ValueError:
                print("solo numeros")
                continue
except:
    print("solo numeros")
print("el promdeio de los numeros pares =",sum(promediopares)/len(promediopares))
print("el promdeio de los numeros impares =",sum(promedioimpares)/len(promedioimpares))


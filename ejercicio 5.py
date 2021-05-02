entero = ""
decimal =""
while True:
    try:
        numero = input("numero = ")
        float(numero)
    except ValueError:
        print("solo numeros o utiliza un punto en vez de una coma")
        continue
    coma = False
    for x in numero:
        if coma:
            decimal +=x
        elif x == ".":
            coma = True
        else:
            entero +=x
    break
print("la parte entera es",entero,)
print("la parte decimal es",decimal)


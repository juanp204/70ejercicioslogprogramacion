while True:
    try:
        km =5000*float(input("cuantos km a recorrer = "))
        dias = float(input("dias de estancia = "))
        if km<100000:
            print("se le cobra lo minimo 100000 peses")
        else:
            if dias>7:
                print("se le va a cobrar",km-(km*0.15))
            else:
                print("se le va a cobrar ",km)
        break
    except ValueError:
        print("solo numeros")
        continue


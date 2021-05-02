while True:
    try:
        lado = float(input("ingrese lado del Hexagono = "))
        altura = float(input("ingrese Altura del Hexagono= "))
    except:
        print("solo nueros")
        continue
    print("el Área del hexagono es ",((lado*6)*altura)/2)
    break


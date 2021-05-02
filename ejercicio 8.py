while True:
    try:
        radio = float(input("diametro del circulo = "))
    except ValueError:
        print("solo numeros")
        continue
    print("el perimetro es",6.283*radio,"y el Área es",3.1416*radio**2)
    break

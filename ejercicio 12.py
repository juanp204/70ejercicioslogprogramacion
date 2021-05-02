while True:
    try:
        altura = float(input("altura = "))
    except:
        print("solo numeros")
        continue
    print(((altura*2)/9.8)**0.5)
    break

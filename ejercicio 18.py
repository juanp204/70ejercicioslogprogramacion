while True:
    try:
        segundos = int(input("segundos = "))
    except:
        print("solo numeros")
        continue
    print(segundos,"a horas es",(segundos/3600))
    break

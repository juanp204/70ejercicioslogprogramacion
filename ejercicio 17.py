while True:
    try:
        segundos = int(input("segundos = "))
    except:
        print("solo numeros")
        continue
    print(segundos,"seg a horas es",segundos/3600)
    break


while True:
    try:
        segundos = int(input("segundos = "))
    except:
        print("solo numeros")
        continue
    print("{}:{}:{}".format(segundos//3600,(segundos%3600)//60,(segundos%3600)%60))
    break


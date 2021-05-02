while True:
    try:
        masa = float(input("masa en KG= "))
    except:
        print("solo numeros")
        continue
    print("la energia cinetica es",(masa*(299792458**2))/2,"J")
    break



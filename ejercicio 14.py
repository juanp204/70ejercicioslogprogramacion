while True:
    try:
        tiempo = float(input("tiempo en seg = "))
        aceleracion = float(input("aceleración en m/s2= "))
        velocidadi = float(input("velocidad inicial m/seg= "))
    except:
        print("solo numeros")
        continue
    print("la velocidad final es",(velocidadi)+(aceleracion*tiempo),"m/s")
    break


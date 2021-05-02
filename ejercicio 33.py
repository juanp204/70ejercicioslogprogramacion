while True:
    try:
        ano = int(input("escriba el año = "))
        break
    except ValueError:
        print("solo numeros")
        continue
print("Es bisiesto" if not ano % 4 and (ano % 100 or  not ano % 400) else "No es bisiesto")


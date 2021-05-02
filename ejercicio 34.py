while True:
    try:
        a = int(input("A = "))
        b = int(input("B = "))
        c = int(input("C = "))
    except ValueError:
        print("solo numeros")
        continue
    try:
        print("las soluciones son",(-b+(((b**2)-(4*a*c))**(0.5)))/(a*2),(-b-((b**2-(4*a*c))**(0.5)))/a*2)
        break
    except:
        print("solucion no valida")
        break


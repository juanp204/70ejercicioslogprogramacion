while True:
    try:
        dinero = int(input("dinero = "))
    except:
        print("solo numeros")
        continue
    print("""1000 = {}
2000 = {}
5000 = {}
10000 = {}
20000 = {}
50000 = {}""".format(((((dinero%50000)%20000)%10000)%5000%2000)//1000,(((dinero%50000)%20000)%10000)%5000//2000,(((dinero%50000)%20000)%10000)//5000,((dinero%50000)%20000)//10000,(dinero%50000)//20000,dinero//50000))
    break

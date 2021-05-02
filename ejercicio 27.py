notas = []
for x in range(5):
    while True:
        try:
            num=float(input("nota "+str(x+1)+"= "))
            if num>=0 and num<=5:
                notas.append(num)
                break
            else:
                print("solo notas entre 0 y 5")
                continue
        except:
            print("solo numeros")
            continue
notaf = ((notas[0]*3)+(notas[1]*4)+(notas[2]*3)+(notas[3]*6)+(notas[4]*4))*0.05
if notaf<2:
    print("no puede habilitar")
elif notaf<3:
    print("reprobo")
elif notaf>4.5:
    print("aprobo, felicidades sacaste una muy buena nota")
else:
    print("aprobo,mediocre")


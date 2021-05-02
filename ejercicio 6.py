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
print("su nota final es",((notas[0]*3)+(notas[1]*4)+(notas[2]*3)+(notas[3]*6)+(notas[4]*4))*0.05)
while True:
    try:
        n = int(input("cuantos numeros = "))
        break
    except ValueError:
        print("solo numeros")
        continue
for x in range(1,n,2):
    print(x, end=" -{} ".format(x+1))
if n%2:
    print(n,end="")



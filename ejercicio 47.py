print("muestra los numeros entre los numeros")
while True:
    try:
        n = int(input("n = "))
        m = int(input("m = "))
        if n>m:
            for x in range(m+1,n):
                print(x, end=" ")
        if m>n:
            for x in range(n+1,m):
                print(x,end=" ")
        break
    except ValueError:
        print("solo nuemros")
        continue


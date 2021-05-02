print("por temas de reforma tributaria el iva va a subir no mas un poco mas del 200% ;), por lo que si el resultado es mayor del que esperaba culpe al gobierno")
precio = int
iva = 200
while True:
    try:
        precio = int(input("precio = "))
        break
    except:
        print("solo numeros")
        continue
if precio>=150000:
    print("precio normal es",precio," - el valor del iva es {}%".format(iva)," - el precio final con descuento es",((precio*(iva-5))/100)+precio)
else:
    print("precio normal es", precio, " - el valor del iva es {}%".format(iva), " - el precio final es",((precio * iva) / 100) + precio)
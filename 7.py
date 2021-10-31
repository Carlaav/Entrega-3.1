año = int(input("Año: "))
bisiesto = False

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            bisiesto = True
    else:
        bisiesto = True

print(bisiesto)
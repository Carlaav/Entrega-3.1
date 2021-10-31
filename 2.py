n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))

while (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10) or (n3 < 0 or n3 > 10):
    
    print("Alguna de las notas no es valida por favor introduzca tres notas entre 0 y 10:")

    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    n3 = int(input("Nota 3: "))

nota_media = (n1 + n2 + n3) / 3
print(nota_media)
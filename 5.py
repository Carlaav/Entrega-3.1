precio_en_litros = 1.3

galones = int(input("Galones surtidos: "))
#Cambio de un litro a galon
litros = galones * 3.78
precio = litros * precio_en_litros

print("El precio es de ", precio)
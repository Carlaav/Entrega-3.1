from random import randint as rd

number_to_guess = rd(0, 300)

guess = int(input("Introduzca su prediccion: "))
while guess != number_to_guess:
    if guess > number_to_guess:
        print("El numero buscado es mas pequeño.")
    else:
        print("El numero buscado es mas grande.")
    guess = int(input("Introduzca su prediccion: "))

print("BIEN HECHO, el numero era", number_to_guess)
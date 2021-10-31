respuestas_correctas = int(input("Acertadas: "))
respuestas_incorrectas = int(input("Incorrectas: "))
respuestas_blanco = int(input("No contestadas: "))

puntuacion_final = (respuestas_correctas * 3) + (respuestas_incorrectas * -1)
print(puntuacion_final)
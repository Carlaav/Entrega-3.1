partidos_ganados = int(input("Partidos ganados:"))
partidos_empatados = int(input("Partidos empatados:"))
partidos_perdidos = int(input("Partidos perdidos:"))

puntuacion = partidos_ganados * 3 + partidos_empatados
print(puntuacion)
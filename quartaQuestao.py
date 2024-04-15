# Faça uma lista que tenha 100 números aleatórios entre 0 a 100

import random

listaDeAleatorios = []

for indice in range(0, 101):
    aleatoria = random.randint(0, 100)
    listaDeAleatorios.append(aleatoria)
print(listaDeAleatorios)
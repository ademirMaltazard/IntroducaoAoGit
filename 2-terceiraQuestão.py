# Crie uma lista que tenha 10 valores e some todos eles.
import random

listaDeValores = []
soma = 0

for indice in range(1,11):
    numero = random.randint(0, 100)
    listaDeValores.append(numero)

print(listaDeValores)
for indice in range(0,10):
    soma += listaDeValores[indice]
print('resultado: ',soma)
numero = int(input('digite um numero: '))

print('Tabuada de multiplicação:')
for indice in range(0, 11):
    print(f'{numero} x {indice} = {numero * indice}')

print('Tabuada de subtração:')
for indice in range(0, 11):
    print(f'{numero} - {indice} = {numero - indice}')

print('Tabuada de soma:')
for indice in range(0, 11):
    print(f'{numero} + {indice} = {numero + indice}')

print('Tabuada de divisao:')
for indice in range(1, 11):
    print(f'{numero} / {indice} = {numero / indice}')


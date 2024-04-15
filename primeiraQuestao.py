# Faça duas variáveis numéricas e descubra qual é a maior

n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero:'))

if n1 > n2:
    print(f'O {n1} é maior que o {n2}!')
elif n2 > n1:
    print(f'O {n2} é maior que o {n1}!')

else:
    print(f'Os numeros são iguais!')
# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 14/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Declaração
resposta = ''

print('Os valores não podem ser 0 ')

# Entrada 
a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

# Condicional


if (a + b <= c) or (c + a <= b) or (b + c <= a):
    # print('Não é um triangulo ')
    resposta = 'Não é um triangulo '
elif (a > b and c > b):
    # print('É um triangulo ')
    resposta = 'É um triangulo '
elif (b > a and c > a):
    # print('É um triangulo ')
    resposta = 'É um triangulo '
elif (a > c and b > c):
    # print('É um triangulo ')
    resposta = 'É um triangulo '
elif (a == b == c):
    resposta = 'É um triangulo '
    # print('É um triangulo ')

print(resposta)
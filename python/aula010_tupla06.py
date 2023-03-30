# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 17/01/2023
# Tupla

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('_' * 50)
print('Estrutura de dados: Tupla')
print('_' * 50)

# Declaração
nomes = ()

minha_tupla_1 = ('Rosa', 'Preto', 'Branco')
minha_tupla_2 = (1, 4, 7, 9)
minha_tupla_3 = ('Preto', 23, 1.3, 10, 23, 23,'Azul', 10)

posicao_tupla = minha_tupla_1.index('Preto')
quantidade_tupla = minha_tupla_3.count(23)

print('_' * 50)
print(f'Tupla 1: {minha_tupla_1}')
print(f'Tupla 3: {minha_tupla_3}')
print(f'O Verde esta na posição: {posicao_tupla} ')
print(f'O numero 23 aparece {quantidade_tupla}')
print('_' * 50)
print()
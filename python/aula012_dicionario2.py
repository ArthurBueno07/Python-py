# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 17/01/2023
# Dicionario

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*70)

# Indices iguais
dicionario1 = {'nome:', 'Jonh', 'nome:','Jane'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario2 = {(1, 2) : [1, 2]} 

# MAs não posso ter uma lista como índice e  uma tupla como valor
# dicionario3 = {[1, 2] : {1, 2}}

# Saída 
print('-'*70)
print(dicionario1)
print(dicionario2)
# print(dicionario3)

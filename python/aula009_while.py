# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# While

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Titulo
print('-=' * 24)
print('ESTRUTURA DE CONTROLE: WHILE')
print('-=' * 24)
print()

print()

# Declaração
opcao = 'CRSETE' # Flag

while (opcao != 'crsete'):
    opcao = str(input('Digite um nome: (Crsete - sair) ')).lower()
else:
    print('Você digitou "crsete", fim do programa! ')

print('-=' * 24)
print()
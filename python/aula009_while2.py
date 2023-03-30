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

# Estrutura dencontrole
while (True):

    # Entrada
    nome = str(input('Você é o Cr7? ')).lower()

    # Condicional
    if (nome != 'champions' ):
        print('Hum... não é você...')
    else:
        print('=-'*24)
        print('Haha é você mesmo!')

        # Interrompe laço
        break
print('=-' * 24)
print()
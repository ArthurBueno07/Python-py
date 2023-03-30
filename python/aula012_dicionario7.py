# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 27/01/2023
# Dicionario

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*70)

# Declaração
agenda = {
    'Negan': 988687337, 
    'Naruto': 98857516569,
    'Pam': 98877441122, 
    'Goku':  9875656589,
    'Wenkend': 98565155
}

print()
print(agenda)
print()

if 'Naruto' in agenda:
    print('Primeiro teste: Verificando se Naruto esta na agenda ')
    print('VERDADEIRO! Naruto esta na agenda ')
else:
    print('FALSO! Naruto não esta na agenda ')

print()

if 'Goku' not in agenda:
    print('Segundo teste: Verificando se Vegeta não esta na agenda ')
    print('VERDADEIRO! Vegeta não esta na agenda ')
else:
    print('Vegeta esta na agenda ')
print('-'*70)
print()

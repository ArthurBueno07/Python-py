# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 26/01/2023
# Dicionario

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*70)

agenda = {
    'Russel': 998856965,
    'Darios': 998877456,
    'Yashuo': 988556633,
}

# Antes
print('- antes:')
print(agenda)

# Copia a chave e o valor e exclui o dicionario de origem
nova_agenda = agenda.popitem()
print()

# Depois
print('- Depois:')
print(agenda)
print()

# Imprimindo a Tupla
print(f'Tupla retornada: {nova_agenda}')
print('-'*70)
print()

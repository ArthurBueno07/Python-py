# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 27/01/2023
# Dicionario

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*80)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*80)

agenda_1 = {
    'nome': 'PamPam',
    'endreço': 'Paris, França',
    'celular': '32 97777-7777'
}

print()
print('- Antes da atualização')
print(agenda_1)

# Criando segunda agenda
agenda_2 = {
     'nome': 'PamPam',
    'endreço': 'Paris, França, 7',
    'celular': '32 97777-7777'
}

# Atualizando a agenda
agenda_1.update(agenda_2)

print()
print('Depois da atualização')
print(agenda_1)
print('(*(-)*)'*11)


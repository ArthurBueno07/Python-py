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

# Declaração
agenda = {
    'nome': 'Goku',
    'cpf': '168.158.499-47',
    'cep': '36057-250',
    'celular': '(32)9.9196-7070',
}

# Pegando chaves, valores e items 
chaves = agenda.keys()
valores = agenda.values()
items = agenda.items()

# Verificando o tamanho da agenda
tamanho = len(agenda)

# Saída
print('-'*120)
print(f'- Todas as chaves da agenda: \n{chaves}')
print()
print(f'- Todos os valores da agenda \n{valores}')
print()
print(f'- Todos os items da agenda \n{items}')
print('-'*120)
print()

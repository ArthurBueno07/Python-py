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
    'Neymar': '32 98865865',
    'Messi': '32 922556898',
    'Cristiano Ronaldo' : '32 966335577',
    'Ribamar': '21 55896932',
    'Sassá': '21 8877441133',
    'Tiquinho': '21 98856571234'
}

# Apagando elemento
del(agenda['Messi'])
del(agenda['Sassá'])
del(agenda['Tiquinho'])

# verificando o tamanho da agenda
tamanho = len(agenda)

# Saída
print('_'*70)
print(agenda)
print(f'O tamnho da agenda é: {tamanho}')
print()

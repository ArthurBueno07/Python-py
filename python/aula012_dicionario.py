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

# Declaração
compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Aatribuindo valores
compras['id'] = 7
compras['item'] = 'chuteira'
compras['valor'] = 250.00

pessoas['id'] = 12
pessoas['nome'] = 'Agostinho Neymar Cristiano Messi'
pessoas['endereço'] = 'Nilton Maracanã'
pessoas['numero'] = 1985
pessoas['cidade'] = 'Juiz de Rio'
pessoas['pais'] = 'Brasil'

cores['black'] = 'Preto'
cores['green'] = 'Verde'
cores['ping'] = 'Rosa'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 710
numeros[2] = 610
numeros[3] = 510

# Saída simples
print(f'Minhas compras: {compras}')
print(f'jogador: {pessoas}')
print(f'Cores RGB: {cores}')
print(f'Tabela periodica: {elementos}')
print(f'Lista de números: {numeros}')
print()
print('-'*70)




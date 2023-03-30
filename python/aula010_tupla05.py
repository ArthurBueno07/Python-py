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

# Declaaração
nomes = ()

# Convertendo tupla em lista
listaNomes = list(nomes)

# Entrada de dados
for c in range(0, 4, 1):
    listaNomes.append(str(input('Digite seu  nome: ')))

# Convertendo lista em tupla
nomes = tuple(listaNomes)

# Saida
print('Nomes: \t', end='    ')
for indice, nome in enumerate(nomes):
    print(f'{indice} : {nome} ', end='  ')

print('_'*50)
print()

nome = str(input('Nome para remover da tupla '))
if (nome not in nomes):
    print('Nome não esta na tupla ')
else:
    # Convertendo a tupla em lista
    listaNomes = list(nomes)
    listaNomes.remove(nome)

    # Convertendo lista em tuplas
    nomes = tuple(listaNomes)

# Saída
print('Nomes: \t', end=' ')
for indice, nome in enumerate(nomes):
    print(f'{indice} : {nome}', end='   ')

print()
print('_'*50)
print()

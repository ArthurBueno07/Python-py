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

# Declaração
numeros = (1, 2, 3, 4, 5, 6) #inteiros
atores = ('Silvester Stalonne', 'Neymara Junior', 'Agostinho Arthur')
personagens =('Goku', 'Naruto', 'Vegeta', 'Saitama')
decimais = (1.2, 2.5, 3.5, 8.7)
mix = ('Cristiano', 1, 55.8, True)

# Saida
print('Numeros; \t ', end=' ')
for indice, numero in enumerate(numeros):
    print(f'{indice} : {numero}', end='        ')
print()

print('atores; \t ', end=' ')
for indice, ator in enumerate(atores):
    print(f'{indice} : {ator}', end='        ')
print()

# Varrendo  as tuplas restantes!

print('_'* 50)
print()


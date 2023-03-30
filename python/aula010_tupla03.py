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
print('Numeros: ', end=' ')
for numeros in numeros:
    print(numeros, end=' ')
print()

print('Atores: ', end=' ')
for atorAtriz in atores:
    print(atorAtriz, end=' ')
print()

print('Personagens:, ', end=' ')
for personagens in personagens:
    print(personagens, end=' ')
print()

print('_'*50)
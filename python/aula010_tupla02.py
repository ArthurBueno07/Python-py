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

# Condicional
if (3 in numeros and 'Goku' in personagens):
    resposta = 'Estão contidos em numeros e personagens!'
else:
    resposta = 'Não estão contidos em numeros e personagens!'

if ('Neymar Junior' not in atores and 1.2 in decimais):
    resposta2 = 'Não esta contido em atores e decimais!'
else:
    resposta2 = 'Esta contido em atores e decimais!'


print(resposta)
print(resposta2)
print('_' * 50)

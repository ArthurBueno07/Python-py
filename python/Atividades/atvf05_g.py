# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 22/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

# Declarando variavel
resposta = ''

# Entrda
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
print('='*50)

# Operação do delta
delta = b **2 - (4*a*c)
x_um = (-b + math.sqrt(delta)) / (2 * a)
x_dois = (-b - math.sqrt(delta)) / (2 * a)

# Saida

print(f'O resultado de x1 é: {x_um}')
print(f'O resultado de x2 é: {x_dois}')
    
print('='*50)

    
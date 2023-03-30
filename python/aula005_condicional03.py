# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 10/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'Cr7'
d = 'Cr7'

print('-'*40)
print('ESTUDO DE CONDICIONAIS: OPERADORES RACIONAIS ')
print()

# Operador == (Igualdade)
if (c == d):
    print('-'*40)
    print(f'{c} é igual {d}') 
    print('-'*40)
else:
    print(f'{c} não é igual a {d}')

# Operador != (diferença)
if (a != c):
    print('-'*40)
    print(f'{a} é diferente a {c}')
    print('-'*40)
else:
    print(f'{a} não é diferente a {c}')

# Operador > (maior que)
if (a > b):
    print('-'*40)
    print(f'{a} é maior que {b}')
    print('-'*40)
else:
    print(f'{a} não é maior que {b}')

# Operador < (menor que)
if (a >= b):
    print('-'*40)
    print(f'{b} é menor que {a}')
    print('-'*40)
else:
    print(f'{b} não é menor que {a}')

# Operador >= (maior ou igual)
if (a >= b):
    print('-'*40)
    print(f'{a} é maior ou igual a {b}')
    print('-'*40)
else:
    print(f'{a} não é maior ou igual a {b}')

# Operador <= (menor ou igual)
if (a >= b):
    print('-'*40)
    print(f'{b} é menor ou igual a {a}')
    print('-'*40)
else:
    print(f'{b} não é menor ou igual a {a}')
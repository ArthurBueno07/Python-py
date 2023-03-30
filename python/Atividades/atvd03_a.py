# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 08/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

# Calculos
# SOMA
soma = a + b + c
# MULTIPLICAÇÃO
produto = a * b * c

# Saída
print('='*70)
print(f'A soma de {a} + {b} + {c} = {soma}')
print(f'O produto de {a} x {b} x {c} = {produto}')

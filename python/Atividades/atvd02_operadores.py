# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 08/11/2022
# Operadores Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
a = float(input('Digite seu primeiro numero: '))
b = float(input('Digite seu segundo numero: '))

# calculos
# soma
soma = a + b
# subtração
subtracao = a - b
# produto
produto = a * b
# divisao 
divisao = a / b
# potencia 
potencia = a ** b
# Divisão Inteira
divisaoInteira = a // b 
# Resto da divisão 
restoDivisao = a % b
# Raiz Quadrada
raiz = soma ** (1/2)
# Raiz Cúbica
raizi = soma ** (1/3)

# Saída
print('-'*70)
print('ESTUDO DE OPERADORES ARITMÉTICOS')
print('='*70)
print(f'A soma de {a} + {b} = {soma}')
print(f'A subtração de {a} - {b} = {subtracao}')
print(f'A multiplicação de {a} x {b} = {produto}')
print(f'A divisão de {a} / {b} = {divisao:.4f}')
print(f'O numero {a} elevado a {b} = {potencia}')
print(f'A divisão de {a} por {b} = {divisaoInteira}')
print(f'O resto da divisão de {a} por {b} = {restoDivisao}')
print(f'Raiz quadrada de {soma} = {raiz}')
print(f'Raiz cubica de {soma} = {raizi}')

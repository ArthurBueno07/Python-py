# Agostinho 
# 18/11/2022
# teste

# Bibbliotecas
import os

# Limpando terminal
os.system('cls')

# Entrada

salario = float(input('Digite seu salario: '))

# Operação
novo_salario = (10 / 100) * salario
novo_salarioo = (5 / 100) * salario

# Condicional
if (salario >= 1500):
	print(f'Seu salario vai ter um aumento de: {novo_salarioo} ')

elif (salario <= 1000):
	print(f'Seu salario vai ter um aumento de: {novo_salario} ')

# Calculo
a = novo_salarioo + salario
b = novo_salario + salario


sim = input('Voce quer saber valor bruto? ')

if (sim == sim):
	print(f'{a}')

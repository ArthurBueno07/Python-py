# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 09/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
base = float(input('Qual a base do retângulo? '))
altura = float(input('Qual a altura do retângulo? '))

# Calculos
p = 2 * (base + altura)


# Saida 
print(f'O perimetro do retângulo é: {p:.0f}')
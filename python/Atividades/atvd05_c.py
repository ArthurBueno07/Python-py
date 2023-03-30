# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 21/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

# Entrada
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

# Operação
resultado = math.pow(base, expoente)

# Saida
print(f'O resultado é: {resultado} ')
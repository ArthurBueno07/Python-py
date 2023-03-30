# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# For...Ranger

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Titulo
print('='*50)
print('ESTRUTURA DE CONTROLE SOMATORIO')
print('='*50)

print()

# Declaração
soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 1}º numero: '))
    
    # Cálculo
    soma += numero # mesma coisa: soma = + numero

print('='*50)
print(f'A soma dos números é: {soma}')
print('='*50)
print()
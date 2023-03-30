# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 08/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

print('Vamos calcular sua idade!? ')
print('~'*70)

# Declaração
ano_atual = 2022

# Entrada
ano = float(input('Digite o ano que você nasceu: '))

# Calculos
idade = ano_atual - ano

# Saída 
print(f'Sua idade é: {idade}')
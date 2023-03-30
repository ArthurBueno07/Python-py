# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 14/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
ano = int(input('Digite um ano: '))

# Condicional
if (ano <= 0):
    print('Ivalido')
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Ano Bissexto ')
else:
    print('Ano normal')

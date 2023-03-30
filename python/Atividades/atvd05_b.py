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
a = float(input('Digite o primeiro numero: ' ))
b = float(input('Digite o divisor do primeiro numero: '))

# Condicional
if(b == 0):
  print('Error')
else:
  resultado = a / b

# Saida
print(f'O Resultado é: {resultado}')
print('Arredondando fica: ')
print(round(resultado))



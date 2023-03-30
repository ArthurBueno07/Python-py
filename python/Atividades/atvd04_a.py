# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 11/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
a = int(input('Digite um numero inteiro: '))


# Condicional
if  (a % 2) == 0:
    print(f'O numero {a} é par')
else:
    print()
    print(f'O numero {a} é impar')

# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 14/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')


# Entrada
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

# Condicional

if (a == 0):
    print('Não existe ')

else:
    delta = (b**2 - 4*a*c)
    x1 = (-b + (delta ** (1/2))) / 2 * a  
    x2 = (-b - (delta ** (1/2))) / 2 * a 
    print(f'A resposta do x1 é {x1}')
    print(f'A resposta do x2 é {x2}')





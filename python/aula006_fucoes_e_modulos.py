# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 18/11/2022
# Funções

# Importando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('='*50)
print()

# Declarações 
base = int(input('Digite a base da potencia: '))
expoente = int(input('Digite o expoente da basa: '))
angulo = float(input('Digite um angulo: '))
radicando = int(input('Digite o numero que você deseja achar a raiz '))
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

# Cálculo
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
Seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)
print('='*50)

# Saida
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno de {angulo} é: {Seno}')
print(f'O cosseno de {angulo} é: {cosseno}')
print(f'O tangente de {angulo} é: {tangente}')
print(f'O valor da hipotenusa é: {hipotenusa}')
print('-'*50)
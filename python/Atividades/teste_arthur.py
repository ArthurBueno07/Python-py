# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 19/11/2022
# Calculadora

# Importando as bibliotecas
import os
from datetime import datetime
from datetime import date
import math

# Limpando o terminal
os.system('cls')

# Direcionamento

print('='*70)
print('Olá!')
print('Bem vindo a calculadora Bueno')
print('='*70)
print('Escolha uma dessas opções:')
print('SOMA = 1')
print('SUBTRAÇÃO = 2')
print('MULTIPLICAÇÃO = 3')
print('DIVISÃO = 4')
print('RAIZ QUADRADA = 5')
print('RAIZ CUBICA = 6')
print('POTENCIA = 7')
print('='*70)


# Variaveis

mais = '1'
menos = '2'
produto = '3'
divisao = '4'
raizQuadrada = '5'
raizcubica = '6'
potencia = '7'

# Entrada de dados

a = input('Você deseja fazer qual operação? ')

# Condicional

if (a == mais):
    print('Beleza vamos la... ')
    numero_um = int(input('Digite um numero: '))
    numero_dois = int(input('Digite o segundo numero: '))
    soma = numero_um + numero_dois
    print(f'O resultado é: {soma}') 

else:

 if (a == menos):
    print('Beleza vamos la... ')
    numero_um = int(input('Digite um numero: '))
    numero_dois = int(input('Digite o segundo numero: '))
    subtracao = numero_um - numero_dois
    print(f'O resultado é: {subtracao}') 

if (a == produto):
    print('Beleza vamos la... ')
    numero_um = float(input('Digite um numero: '))
    numero_dois = float(input('Digite o segundo numero: '))
    multiplicacao = numero_um * numero_dois
    print(f'O resultado é: {multiplicacao}') 

if (a == divisao):
    print('Beleza vamos la... ')
    numero_um = float(input('Digite um numero: '))
    numero_dois = float(input('Digite o segundo numero: '))
    divi = numero_um / numero_dois
    print(f'O resultado é: {divi:.4f}') 

if (a == raizQuadrada):
    print('Beleza vamos la... ')
    numero_um = int(input('Digite o numero que você deseja achar a raiz: '))
    resultado = numero_um ** (1/2)
    print(f'A raiz quadrada de {numero_um} é: {resultado}')

if (a == raizcubica):
    print('Beleza vamos la... ')
    numero_um = int(input('Digite o numero que você deseja achar a raiz: '))
    resultado = numero_um ** (1/3)
    print(f'A raiz quadrada de {numero_um} é: {resultado}')

if (a == potencia):
    print('Beleza vamos la... ')
    numero_um = float(input('Digite um numero: '))
    numero_dois = float(input('Digite o expoente: '))
    resultado = numero_um ** numero_dois
    print(f'O resultado é: {resultado}') 
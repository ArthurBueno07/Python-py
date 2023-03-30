# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 11/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
print('-'*50)

# Condicional
if (a > b and a > c):
    print(f'Esse é o maior numero: {a} ')

elif (b > a and b > c):
    print(f'Esse é o maior numero: {b} ')

elif (c > a and c > b):
    print(f'Esse é o maior numero: {c} ')

if(a == b and a != c):
    print(f'Esses numeros são iguais: {a} e {b} ')

elif(b == c and b != a):
    print(f'Esses numeros são iguais: {b} e {c} ')

elif(c == a and c != b):
    print(f'Esses numeros são iguais: {c} e {a} ')

elif(c == a and c == b):
    print(f'São iguais: {a}, {b} e {c} ')

if(a < b and a < c):
    print(f'Esse é o menor numero: {a} ')

elif(b < c and b < c):
    print(f'Esse é o menor numero: {b} ')

elif(c < a and c < b):
    print(f'Esse é o menor numero: {c} ')
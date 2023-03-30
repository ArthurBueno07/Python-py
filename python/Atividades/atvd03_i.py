# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 09/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Declaração
dolar = 0.192870

# Entrada
a = float(input('Quantos reais você irá converte? BRL = '))

# Calculos
resultado = a * dolar

# Saída
print(f'O tanto que você ira ter em dolar será: USD {resultado:.2f}')
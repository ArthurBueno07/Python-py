# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 11/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Entrada
velocidade =  int(input('O carro passou em qual velocidade? '))

# Condicional
if (velocidade > 60):
    print(f'Limite de velocidade acima do permitido')
elif (velocidade <= 60):
    print(f'Velocidade normal!')



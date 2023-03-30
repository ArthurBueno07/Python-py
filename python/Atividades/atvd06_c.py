# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 25/11/2022
# Atividade 06  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declarando variavel
resposta = ''

# Entrada
nome = str(input('Digite seu nome completo: '))

# Operação
if ('Oliveira' in nome):
    resposta = 'True'
else:
    resposta = 'False'

# Saida
print(resposta)
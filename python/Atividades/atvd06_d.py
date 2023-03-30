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

frase = 'Eu sou lindo!'

maiuscula = frase.upper()
minuscula = frase.lower()
quantidade = len(frase)
a = frase[2:5]
# Saida
print(f'Frase maiuscula: {maiuscula}')
print(f'Frase minuscula: {minuscula}')
print(f'Quantidade de caracteres na frase: {quantidade}')
print(f'Quantidades de caracteres na segunda palavra: {len(a)}')
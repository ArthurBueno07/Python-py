# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 18/11/2022
# Datetime

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('Trabalhando com Strings: Funções')
print('='*50)

# Declaração
variavel_str = 'Estou estudando Python '

resultado_do_replace = variavel_str.replace('Python','Java')

resposta = ''

if ('estudando' in variavel_str):
    resposta = 'Verdadeiro'
else:
    resposta = 'Falso'

print(f'String original: {variavel_str}')
print(f'Quantidade de caracteres: {resultado_do_replace}')
print(f'Exista a palavra "estudando" na string "{variavel_str}":{resposta}')
print('='*50)
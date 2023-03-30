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
frase = str(input('Digite um frase: '))

# Operação
start = 'a'
vogais = frase.count(start, 0, 100)


# Saida
print(f'O numero de vogais é: {vogais}')
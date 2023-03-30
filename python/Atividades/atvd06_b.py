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
nome = 'João Silva'

nome_trocado = nome.replace('Silva', 'Oliveira')

# Saida
print(f'Nome original: {nome}' )
print(f'Nome trcado: {nome_trocado}')
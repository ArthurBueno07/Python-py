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

# Entrada de dados
nome = str(input('Digite o seu primeiro nome: '))
nome_do_meio = str(input('Digite o nome do meio: '))
sobrenome = str(input('Digite o sobrenome: '))

lista = [nome, nome_do_meio, sobrenome]

juntar_string = ' '.join(lista)

print(juntar_string)
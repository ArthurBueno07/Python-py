# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

contador = 0
numero = 0
numero_dois = 0

numero = int(input('Digite um numero '))
numero_dois = int(input('Digite ate onde irá contar: '))
for contador in range(numero, numero_dois):
    print(contador)
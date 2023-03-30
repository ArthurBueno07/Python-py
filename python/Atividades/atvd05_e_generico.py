# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 22/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import random

# Limpando o terminal
os.system('cls')

# Declarando variaveis
lista_de_nomes = ['Neymar','Messi', 'Cr7']
lista_dicionario = [{"Nome": "Neymar", "idade": 27}, {"Nome": "Messi", "idade": 34},
{"Nome": "Cr7", "idade": 36}]

# Saida
random.seed()

print(random.randint(1, 20)) # Definindo numeros para ser sorteados

print(random.choice(lista_de_nomes))

print(random.choice(lista_dicionario))

nivel = 0

while (nivel < 1 or nivel > 3):
    nivel = int(input("Digite um nível: "))

    if (nivel == 1):
      tentativas = 20
    elif (nivel == 2):
      tentativas = 10
    elif (nivel == 3):
      tentativas = 5
    else:
     print("Digite uma opção válida.")
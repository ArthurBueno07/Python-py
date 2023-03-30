# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 06/12/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
contador = 0
numero_1 = 0
numero_2 = 0

# Entrada
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

# Operação e Saída
for contador in range(numero_1, numero_2):
    if (contador == 8 or contador == 2 or contador == 25):
        continue
    else:
        print(contador)

    
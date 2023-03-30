# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 22/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

# Entrada 
angulo = float(input('Digite um ângulo: '))

# Calculo
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saida
print(f'O seno de {angulo} é: {seno:.2f} ')
print(f'O cosseno {angulo} é: {cosseno:.2f} ')
print(f'A tagente {angulo} é: {tangente:.2f} ')

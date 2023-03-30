# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 22/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import random

# Limpando o terminal
os.system('cls')

# Declarando variavel
resultado = ''

# Entrada
numero = int(input('Tente acerta o numero que o computador esta pensando: '))

# Sorteio
a = random.randint(1, 10)

print(f'Esse foi o numero sorteado: {a} ')

# Condicional
if (numero == a):
    resultado = 'Parabéns você acertou!'
else:
    resultado = 'Que pena, você errou...'

# Saida
print(resultado)

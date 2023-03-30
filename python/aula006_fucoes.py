# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 18/11/2022
# Funções

# Importando as bibliotecas
import os
import random

# Importando as biblioteca da função
import math

# Especificando o import
from math import sqrt

# Limpando o terminal
os.system('cls')

# Utilização

numero = int(input('Digite um numero: '))

# Para import da biblioteca toda
raizQuadrada = math.sqrt(numero)

# Para um import especifico
raizQuadrada = sqrt(numero)

print(f'A raiz é: {raizQuadrada}')
# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 17/01/2023
# Set

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('_'*50)
print('ESTRUTURA DE DADOS: SET')
print('_'*50)

# Método remove()
print()
frutas = {"Maçã", "Uva", "Banana", "Kiwi"}

print('_'*50)
print(f'Fruta antes: {frutas}')
# Coloque um valor diferente para testar erro
frutas.remove('Maçã')
print(f'Frutas depois: {frutas}')

# Método discard ()
print()
numeros = {20, 30, 40, 50, 60}

print()
print('_'*50)
print(f'Numeros antes: {numeros}')
# Coloque um valor diferente para testar o error 
numeros.discard(30)
print(f'Numeros depois: {numeros}')
print()
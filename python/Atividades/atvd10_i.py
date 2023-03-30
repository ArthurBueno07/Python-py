# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 27/12/2022
# Atividade 10  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
elemento = {
    'Elemento 1':'Água',
    'Elemento 2':'Fogo',
    'Elemento 3':'Terra',
    'Elemento 4':'Ar'
    }

# Saída
print(f'Antes: {elemento}')
print('-'*50)
del(elemento['Elemento 4'])

print('-'*50)
print(f'depois: {elemento}')
print('='*50)
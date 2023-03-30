# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 27/12/2022
# Atividade 10  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

nomes = {
    'nome':'Jorge',
    'idade': 25,
    'peso': 82,
    'altura': 1.81
    }

print(f'Dicionario antes: {nomes}')

del(nomes['peso'])

items = nomes.items()

print()
print(f'Dicionario depois: {items}', end=' ')    

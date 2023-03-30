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

# Declaração
nomes = ('Arthur', 'Neymar', 'Cristiano')
numeros = (1, 2, 3, 4, 5, 6, 7)

# Set não tem indice!

# Mas posso varrer com for
for nome in nomes:
    print(nome, end=' ')

print()
print()
print('_'*50)
print('Adicionando elementos Sets')
print('_'*50)

# Não tem função append para Sets!

# Metod add() inserindo itens 
print()
clubes = {"Botafogo", "Vasco", "Fluminense"}

# Inserindo um elemento no Set
print(f'Antes: {clubes}')
clubes.add("Flamengo")
print(f'Depois: {clubes}')

print()
print()
# Metodo Update
clube2 = {"Botafogo", "Vasco", "Fluminense"}

# Inserindo mais de um elemento no set
print(f'Antes: {clube2}')
clube2.update(["Flamengo", "Santos", "Tabajara"])
print(f'Depois: {clube2}')
print()
# Curso tecnico de informatica
# Autor: Agostinho Arthur Bueno fernandes
# Data 19/01/2023
# Atividade 08

# Tupla
# Count

print('-'*50)

# Declaração
nomes = ()

tupla = (25, 5, 6, 58, 89, 25)

quantidade = tupla.count(25)

# Saída
print(f'O numero 25 aparece {quantidade} vezes')
print('-'*50)
print()

# Index
# Declaração
tupla2 = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

posicao = tupla2.index("Botafogo")

# Saída
print(f'O Botafogo aparece na posição {posicao}')
print('-'*50)
print()

# Set
# Remove

# Declaração
jogador = {"Cristiano", "Neymar", "Messi", "Ribamar"}

print(f'A lista de jogadores é: {jogador}')

# Entrada de dados
remover = str(input('Digite o nome do jogador que você desejar retirar: '))

# Saída
jogador.remove(remover)
print(f'Essa é a lista atualizada: {jogador}')
print('-'*50)
print()

# Update

time = {"Real Madrid", "Barcelona", "PSG", "Milan", "Botafogo", "Tabajara"}

print(f'A lista de times é: {time}')

# Entrada de dados
colocar = str(input('Digite o nome do time que você deseja adicionar: '))

# Saída
time.update([colocar])
print(f'Essa é a lista atualizada: {time}')
print('-'*50)
print()

# Pop
# Declaração
nome = {"Arthur", "Jorge", "Tiquinho", "carlos", "Henrique"}
print(f'A lista de nomes é: {nome}')

# Entrada de dados
sair = str(input('Digite o nome que você acha que vai sumir: '))
a = nome.pop()
print(nome)

# Condicional
if sair == a:
   print('Acertou miseravi!')
else:
   print('Você errou!')

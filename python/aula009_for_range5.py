# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# For...Ranger

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Titulo
print('=' * 50)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('=' * 50)

print()

for c in range(1, 11):
    if (c == 5 or c == 7 or c == 10):
        print(f'O número {c} está fora do loop ')
        continue # Salta o ciclo e continua

    print('O número é ' " ➪  " + str(c))

print('⊛' * 50)
print()
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
print('ESTRUTURA DE CONTROLE: BREAK')
print('=' * 50)

print()

for c in range(0, 200):

    print(f'Valor: {c}')

    # Condição para terminar a contagem
    if (c == 200):
        print(f'Contagem interrompida no {c} ')
        break

print('=' * 50)
print('Fim do programa!')
print()
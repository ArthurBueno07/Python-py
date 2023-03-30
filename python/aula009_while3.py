# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# While

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# titulo
print('/'*50)
print('ESTRUTURA DE CONTROLE WHILE ELSE CONTINUE ')
print('/'*50)
print()

# Declaração

contador = 0 # Flag

# Estrutura
while(contador <= 100):

    # Soma o conador
    contador += 7

    # Condicional
    if(contador % 2 == 0):
        continue
    # Imprime o Contador
    print(f'Contador = {contador}')
else:
    print(f'Bloco do while...else {contador}')

print('/' * 50)
print('Fim do programa!')
print()
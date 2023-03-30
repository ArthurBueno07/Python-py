# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 10/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

print('-'*50)
print('Pratica: verificando valor quebrado')
print('-'*50)

# Entrada 
valor = float(input('Digite um valor em casas decimais: '))

# Condicional
if (valor % 1 == 0):
    print(f'valor {valor} invalido! O número digitado é inteiro')
else:
    print()
    print(f'O valor digitado foi {valor}, entrada correta!')

print('-'*50)
print('Fim do programa!')
print('-'*50)
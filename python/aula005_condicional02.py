# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 10/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'Neymar'

# Condicional simples
print('-'*40)
print('Condicional simples')
print('-'*40)
if (a > b):
    print('"a" é maior que "b"!')
else:
    print('"a" não é maior que "b"!')
print()

# Condicional Aninhada
print('-'*40)
print('Condicional Aninhada')
print('-'*40)
if(a < b):
    print('"a" é maior que "b"!')
elif (b != 5):
    print('"b" é diferente de "c"')
elif (c == 'Neymar'):
    print('"c" é igual a "Neymar"')
else:
    print('Se nada deu certo!')
print()
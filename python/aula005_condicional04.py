# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 11/11/2022
# Atividade 03 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'Neymar'

print('-'*40)
print('ESTUDO DE CONDICIONAIS: OPERADORES LOGICOS ')
print('-'*40)
print()

# E (and) VERDAEIRO
print(' E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('falso: Bloco executado')

print()

# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: B') 
else:
    print('Falso: Bloco executado')

print()

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print()

# OU (or) FALSO
print('OU (or) FALSO')
if (a > 5 or b == 'Neymar'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')


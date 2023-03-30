# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 30/11/2022
# For...Ranger

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
soma = 0

# estrutura de Controle
for c in range(0, 5):

    # Entrada de Dados
    numero = input('Digite um número [0-5]: ')

    # Validação
    if (not(numero.isnumeric())):
        print(f'"{numero}" não é um numero! ')
        print()
    else:
        # Casting da variavel, ou seja, vai virar um inteiro
        numero = int(numero)

        # Validando o Intervalo pedido
        if (numero >= 0 and numero <= 5):
            print(f'O número {numero} é valido! ')
            print()
        else:
            print(f'O número {numero} não é valido!')
            print()


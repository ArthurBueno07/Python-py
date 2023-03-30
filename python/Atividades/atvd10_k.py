# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 27/12/2022
# Atividade 10  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
nome_idade = {}
lista = []

# Flag
opcao = '999'

while(True):
    opcao = str(input('Digite "999" para sair, caso queira ignorar é so aperta o enter: '))

    if (opcao != '999'):
        nome_idade['nome'] = str(input('Digite seu nome: '))
        nome_idade['idade'] = int(input('Digite sua idade: ')) 
        lista.append(nome_idade.copy())
        print('Digite mais um nome e idade... ')
    else:
            print('Você digitou "999" para sair ')

            break
            print('-'*50)

print(f'Essa é a lista de nomes e idade {lista}')

    
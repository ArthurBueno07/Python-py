# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 07/11/2022
# Atividade 01 Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')


# Entrada
print('Seja Bem Vindo ao cadastro do Eroios')
print('Irei te pedir alguns dados!')

nome = str(input('Digite seu nome completo: '))
data_nas = int(input('Digite sua data de nascimento: '))
rg = int(input('Digite seu o seu RG: '))
cpf = int(input('Digite seu CPF: '))
print('='*70)
print('ENDEREÇO')
print('='*70)
rua = str(input('Digite o nome da sua rua: '))
nmr = int(input('Digite o numero da sua casa: '))
complemento = str(input('Digite um complemento: '))
cep = int(input('Digite seu CEP: '))
cidade = str(input('Digite o nome da sua ciddade: '))
estado = str(input('Digite o nome do seu estado: '))
print('='*70)


# Saída
print('Nome: ', nome)
print('Data de nascimento: ',data_nas)
print('RG: ',rg)
print('CPF: ',cpf)
print('='*70)
print('ENDEREÇO')
print('='*70)
print('Rua: ',rua)
print('Numero da casa: ',nmr)
print('Complemento: ',complemento)
print('CEP: ',cep)
print('Cidade: ',cidade)
print('Estado: ',estado)
print('='*70)
print('OBRIGADO POR PREENCHER!')


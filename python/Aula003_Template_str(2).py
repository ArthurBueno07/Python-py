# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 07/11/2022
# Primeiro Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')


# Entrada
nome = str(input('Nome completo: '))
endereco = str(input('Digite o endereço: '))
cep = int(input('Entre com o cep: '))
cidade = str(input('Digite o nome da cidade: '))
estado = str(input('Entre com o estado: '))
nota_enem = float(input('Digite sua nota no Enem: '))

# Saída Formatada 
print('-'*70)
print('ESTUDO DE SAÍDA FORMATADA')
print('='*70)
print(f'Nome completo {nome}')
print(f'Endereco {endereco}')
print(f'CEP {cep}')
print(f'Cidade {cidade}')
print(f'Estado {estado}')
print(f'Nota da Enem {nota_enem:.2f}')
print('-'*70)
print('FIM DO PROGRAMA!')
print('='*70)
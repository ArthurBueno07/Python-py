# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 26/01/2023
# Dicionario

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*70)

# Declaração
agenda = {
    'Negan': 988687337, 'Naruto': 98857516569,
    'Pam': 98877441122, 'Goku':  9875656589,
    'Wenkend': 98565155
}

# Pegando o elemento do dicionario
busca_1 = agenda.get('Negan','Contato não encontrado')
busca_2 = agenda.get('Vegeta','Contato não encontrado')
busca_3 = agenda.get('Goku','Contato não encontrado')

# Saída
print()
print(f'O celular do Negan {busca_1}')
print(f'O celular do Vegeta {busca_2}')
print(f'O celular do Goku {busca_3}')
print('-'*70)
print()
# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 18/11/2022
# Datetime

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

from datetime import datetime
from datetime import date

# Declarando uma variavel data
data = datetime.now()

# Declarando uma variavel data formatada
data_formatada = data.strftime('%d/%n/%Y')

# Declarando uma variavel data e hora formatada
data_hora_formatada = data.strftime('%d/%n/%Y %H:%M')

print(f'Data formatada: {data_formatada} ')
print(f'data e hora formatdas: {data_hora_formatada} ')

# Recebendo ano
data_atual = date.today()
nascimento = int(input('Digite o ano que você: '))

# Imprimindo só ano
print(f'Ano atual: {data_atual.year}')

idade = data_atual.year - nascimento

# Imprimindo so idade
print(f'Sua idade é: {idade} anos')
# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 07/12/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração 
contador = 0
impares = 0
soma = 0

# Operação e Saída
for contador in range(0, 100):
    if(contador % 2) != 0:
        impares += 1
        soma += contador
        print(contador)
print(f'Foram encontrados: {impares} ')
print(f'A soma dos numeros impares é: {soma}')

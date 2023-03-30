# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 06/12/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
numero_1 = int(input('Verificar numeros primos de: '))
numemor_2 = int(input('Ate: '))
contador = 0
lua = 0


for contador in range(numero_1, numemor_2):
    if  (numero_1>=1):
        for lua in range(2,contador):
            if(contador % lua == 0):
                break
        else: 
            print(contador)       
     
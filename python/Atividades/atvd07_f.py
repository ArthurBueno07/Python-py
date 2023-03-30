# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 06/12/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Declaração
num = int(input('Verificar numeros primos ate: '))
contador = 0
lua = 0


for contador in range(0, num):
    if  (num>=1):
        for lua in range(2,contador):
            if(contador % lua == 0):
                break
        else: 
            print(contador)       
     


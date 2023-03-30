# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 21/11/2022
# Atividade 05  

# Importando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

# Entrada 
raiz = float(input('Digite o numero que você deseja achar a raiz: '))

# Calculo
resultado = math.sqrt(raiz)



# Condicional e saida
if (raiz <= 0):
    print('Não foi possivel realizar sua operação!')

elif (raiz > 1):
    print(f'O resultado {resultado:.4}')
    print(f'Arrendondando fica:' )
    print(round(resultado))







# Obs tenta fazer desse jeito depois

# Condicional
# if (resultado >= (resultado.5)):
    # a = (math.ceil(resultado))
    # print(f'Esse é o Resultado: {a}')

# elif (resultado <= (resultado4)):
    # a = (math.floor(resultado))
    # print(f'Esse é o Resultado: {a}')

    


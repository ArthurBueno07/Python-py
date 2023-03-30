# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 07/12/2022
# Atividade 07  

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

# Entrada 
texto = str(input('Digite um texto ')).lower()
posicao = len(texto)
texto_inverso = ""

# Operação e Saída
while posicao > 0:   
    texto_inverso += texto[posicao -1]
    posicao -= 1
    print(texto_inverso)

if (texto_inverso == texto):
    print('Verdade')
else:
    print('Falso')

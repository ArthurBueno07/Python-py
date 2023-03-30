# Curso Técnico de Informática
# Autor: Agostinho Arthur Bueno Fernandes 
# Data: 14/11/2022
# Atividade 04 Programa Python

# Importando as bibliotecas
import os
# Limpando o terminal
os.system('cls')

a = float(input("Lado a = "))
b = float(input("Lado b = "))
c = float(input("Lado c = "))
 
if (a < b + c and b < a + c and c < b + c):
    if (a == b and b == c):
        print("\nOs lados formam um Triângulo Equilátero.")
    else:
        if (a == b or a == c or b == c):
            print("\nOs lados formam um Triângulo Isósceles.")
        else:
            print("\nOs lados formam um Triângulo Escaleno.")
else:
    print("\nOs lados não formam um triângulo!")
 
sair = input("\nDigite ENTER para sair...")
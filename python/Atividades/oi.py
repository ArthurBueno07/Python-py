c =''
nome = {"Arthur", "Jorge", "Tiquinho", "carlos", "Henrique"}
print(f'A lista de nomes é: {nome}')

sair = str(input('Digite o nome que você acha que vai sumir: '))
a = nome.pop()
print(nome)

while(c == 'Acertou miseravi!'):
    if sair == a:
       c = print('Acertou miseravi!')
    else:
      c =  print('Você errou!')
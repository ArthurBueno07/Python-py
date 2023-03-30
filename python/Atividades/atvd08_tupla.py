# Curso tecnico de informatica
# Autor: Agostinho Arthur Bueno fernandes
# Data 19/01/2023
# Atividade 08

# Tuplas
# Método index()

nomes = ()
tupla = ('Bill', 'Jorge', 'Pedro', 'Genildo')
posicao = tupla.index("Genildo")
print(f'A posição de Genildo é: {posicao}')
print()
print()

# Método count()

tupla_count = ("Verde", "Verde", "Verde", "Preto", "Branco")
quantidade = tupla_count.count("Verde")
print(f'O Verde aprece {quantidade} vezes ')
print()
print()

# Set
# Método remove

set = {"Neymar", "Messi", "Ronaldo", "Sasá"}
print(f'Antes: {set}')
set.remove('Messi')
print(f'Depois: {set}')
print()
print()

# Método discard

set_discard = {"Neymar", "Messi", "Ronaldo", "Sasá"}
print(f'Antes: {set_discard}')
set_discard.discard('Sasá')
print(f'Depois: {set_discard}')
print()
print()

# Método update

set_update = {"Rosa", "Azul", "Verde"}
print(f'Antes: {set_discard}')
set_update.update(["Vermelho", "Cinza"])
print(f'Depois: {set_update}')
print()
print()

# Método union

set0 = {"Banana", "Abacate", "Mamão"}
set1 = {"Limão", "Cebola", "Almerão"}
print(f'Antes: {set0}')
print(f'Antes: {set1}')
set_union = set0.union(set1)
print(f'Depois: {set_union}')
print()
print()

# Método symmetric_difference_update

set0 = {"Banana", "Cebola", "Mamão"}
set1 = {"Limão", "Cebola", "Almerão"}
print(f'Antes: {set0}')
print(f'Antes: {set1}')
set0.symmetric_difference_update(set1)
print(f'Dpois: {set0}')
print()
print()

# Método symmetric_difference

set0 = {"Banana", "Cebola", "Mamão"}
set1 = {"Limão", "Cebola", "Almerão"}
print(f'Antes: {set0}')
print(f'Antes: {set1}')
set_diferent = set0.symmetric_difference(set1)
print(f'Dpois: {set_diferent}')
print()
print()

# Método pop

set_pop = {"apple", "banana", "cherry"}
set_pop.pop() 
print(set_pop)

# Método clear
set_clear = {"Fiona", "Amora", "Pingo"}
print(f'Antes: {set_clear}')
set_clear.clear()
print(f'Depois: {set_clear}')
print()
print()

# Método add

set_add = {"Botafogo", "Real Madrid", "Psg"}
print(f'Antes: {set_add}')
set_add.add("Barcelona")
print(f'Depois: {set_add}')
print()
print()

# Método copy

set_copy = {"Feijão", "Arroz", "Queijo"}
print(f'Antes: {set_copy}')
copy = set_copy.copy()
print(f'Depois: {copy}')
print()
print()

# Método  difference

set_difference = {"apple", "banana", "cherry"}
set_difference1 = {"google", "microsoft", "apple"}
print(f'Antes: {set_difference}')
print(f'Antes: {set_difference1}')
difference = set_difference.difference(set_difference1)
print(f'Depois: {difference}')
print()
print()

# Método difference_update

set_difference_update = {"Ituano", "Manchester", "Paris"}
set_difference_update1 = {"Nova era", "city", "Paris"}
print(f'Antes: {set_difference_update}')
print(f'Antes: {set_difference_update1}')
set_difference_update.difference_update(set_difference_update1)
print(f'Depois: {set_difference_update}')
print()
print()

# Método intersection

a = {"Fogão", "Armario", "Copa"}
b = {"Panela", "Colchão", "Fogão"}
print(f'Antes: {a}')
print(f'Antes: {b}')
c = a.intersection(b)
print(f'Depois: {c}')

# Método intersection_update

a = {"Fogão", "Armario", "Copa"}
b = {"Panela", "Colchão", "Fogão"}
print(f'Antes: {a}')
print(f'Antes: {b}')
a.intersection_update(b)
print(f'Depois: {c}')
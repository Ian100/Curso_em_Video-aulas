# Hoje trataremos sobre LISTAS:
#
# Diferentemente das Tuplas, as LISTAS são MUTÁVEIS!
#
# LISTAS sempre serão representadas por COLCHETES!
#
# Alguns métodos úteis das listas são:
#
#  - O método APPEND(): usado para adidionar um elemento ou objeto ao final de
#  uma lista! Ex: lista.append('Macaco')
#  - O método INSERT(): usado para adicionar um novo elemento à lista na
#  posição desejada! Ex: lista.insert(0, 'Pudim')
#  - O comando del: apaga uma tupla, lista, dicionário ou um elemento das
#  mesmas!
#  - O método POP(): remove um elemento da lista( tem que ser especificado o
#  índice ). Ex: lista.pop(0)
#  Normalmente usado para remover o último elemento de uma lista( não precisa
#  especificar nada )! Ex: lista.pop()
#  - O método REMOVE(): usado também para remover um elemento da lista( porém
#  é necessário especificar o valor do elemento a que se quer remover )!
#  Ex: lista.remove('Macaco')
#  A função LIST(): usada para criar listas!
#  O método SORT(): usado para ordenar os elementos de uma lista
#  ( Padrão: Ordem Crescente ). Ex: valores.sort()
#  Também é possível usá-lo para ordenar os elementos de uma lista
#  na ordem inversa. Ex: valores.sort(reverse=True)
#  A função LEN(): usada para contabilizar a quantidade de elementos de uma
#  tupla, lista, dicionário ou variável!

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor para adicionar à lista: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.\n')

a = [2, 3, 4, 7]
b = a
print('b = a')
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')
b[2] = 8
print('b[2] = 8')
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')
print('Cópia de A:\na = [2, 3, 4, 7]')
print('b = a[:]\nb[2] = 8')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

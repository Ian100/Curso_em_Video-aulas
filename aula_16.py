'''
Existem 3 tipos de variáveis compostas:

- TUPLAS
- LISTAS
- DICIONÁRIOS

Até agora temos usado variáveis simples!
Hoje, estudaremos as TUPLAS!

TUPLAS são variáveis compostas e IMUTÁVEIS que permitem armazenar
vários valores em uma mesma estrutura.

TODA TUPLA FICA ENTRE PARÊNTESES!
TODA LISTA FICA ENTRE COLCHETES!
TODO DICIONÁRIO FICA ENTRE CHAVES!
'''

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
# Na hora de referenciar um elemento, seja de uma tupla, de uma lista, ou de um
# dicionário, use sempre colchetes, como aprendido nas aulas anteriores!
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche)) # O Método SORTED ordena os elementos de uma tupla, lista
# ou dicionário em ordem alfabética!

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(9))
print(c)
print(c.index(8))
print(c.index(4))
print(c.index(2))
print(c.index(2, 4))
print(c.index(5))
print(c.index(5, 1))

pessoa = ('Gustavo', 39, 'M', 99.88) # As Tuplas aceitam vários tipos de dado!
print(pessoa)

del(pessoa) # É possível apagar uma Tupla inteira ou qualquer coisa com o comando
# del() porém é impossível apagar os elementos de uma tupla, visto que ela é
# imutável!

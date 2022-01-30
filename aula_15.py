# Aula 15 - Interrompendo repetições 'WHILE'
'''
Portugol:

enquanto Verdadeiro:  (Esta é uma condição que se repete indefinidamente,
    se chão:           ou seja, um loop infinito!)
        passo
    se não tem chão:
        pula
    se tem moeda:
        pega
    se tem troféu:
        pula
        interrompa
pega

Python:

while True:
    if ground:
        passo
    if not ground:
        pula
    if coin:
        pega
    if trophy:
        pula
        break
pega
'''

# Prática:

# Exercício 1:

cont = 1
while cont <= 10:
    print(cont, '... ', end='')
    cont += 1
print('Acabou!')

while True:
    print(cont, '... ', end='')
    cont += 1
    break
print('Acabou!')

# Exercício 2:

n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))

cont = 0
while cont < 3:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1

s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += n
print('A soma vale {}\n'.format(s))

s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
print('A soma vale {}\n'.format(s))

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}\n')  # Esta é uma FString

# Exercício 3:

# FStrings

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.\n')

salário = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salário}')

salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}')
# É possível usar todo o conteúdo aprendido em manipulação de strings com
# as FStrings do python!

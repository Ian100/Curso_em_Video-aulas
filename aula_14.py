''' ESTRUTURA DE REPETIÇÃO 'ENQUANTO':

    TEORIA:

    Exemplo 1:

    Em Portugol:

    enquanto não chegar na maçã:
        passo
    pega

    Em Python:

    while not apple:
        passo
    pega

    Exemplo 2:

    Em Portugol:

    enquanto não chegar na maçã:
        se tem chão:
            passo
        se não tem chão:
            pula
        se tem moeda:
            pega
    pega

    Em Python:

    while not apple:
        if ground:
            passo
        if hole:
            pula
        if coin:
            pega
    pega
'''

# PRÁTICA:

# Exemplo 1:

'''
   for c in range(1, 10):
       print(c)
   print('Fim')
'''

'''
   c = 1
   while c < 10:
       print(c)
       c += 1
   print('Fim')
'''

# Exemplo 2:

for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')

# Exemplo 3:

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# Exemplo 4:

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

# Exemplo 5:

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

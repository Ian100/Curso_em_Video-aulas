'''AULA 13

LAÇOS DE REPETIÇÃO

Exemplo 1:

laço c no intervalo(1, 10):
    passo
pega

Em Python:

for c in range(1, 10):
    passo
pega

Exemplo 2:

laço c no intervalo(0, 3):
    passo
    pula
passo
pega

Em Python:

for c in range(0, 3):
    passo
    pula
passo
pega

Exmplo 3:

laço c no intervalo(0, 3):
    se tiver moeda:
        pega
    passo
    pula
passo
pega

Em Python:

for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega

Obs.: Intervalo(início, fim, intervalo ou razão)
'''

# PARTE PRÁTICA

''' 
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('FIM')
'''

# Exemplo 1:

for c in range(0, 10):
    print('Oi')
print('FIM')

# Exemplo 2:

for c in range(0, 10):
    print(c)
print('FIM')

# Exemplo 3:

for c in range(6, 0, -1):
    print(c)
print('FIM')

# Exemplo 4:

for c in range(0, 7, 2):
    print(c)
print('FIM')

# Exemplo 5:

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')

# Exemplo 6:

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')

# Exemplo 7:

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

# Exemplo 8:

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O Somatório de todos os valoes foi {}'.format(s))

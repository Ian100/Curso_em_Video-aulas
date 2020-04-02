from math import sqrt
import random
import emoji
n = float(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz de {} é {:.2f}'.format(n, raiz))

n1 = random.random()
print(n1)

print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))

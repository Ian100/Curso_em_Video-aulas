nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

print('Prazer em te conhecer {:20}!'.format(nome))

print('Prazer em te conhecer {:>20}!'.format(nome))

print('Prazer em te conhecer {:<20}!'.format(nome))

print('Prazer em te conhecer {:^20}!'.format(nome))

print('Prazer em te conhecer {:=^20}!\n'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma entre {} e {} é {}!'.format(n1, n2, n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {} !'.format(s, m, d))
print('Divisão inteira é {} e Potência é {} \n'.format(di, e))

print('A soma é {}, o produto é {} e a divisão é {:.3f} !'.format(s, m, d))
print('Divisão inteira é {} e Potência é {} \n'.format(di, e))

print('A soma é {}, o produto é {} e a divisão é {} !'.format(s, m, d), end=' ')
print('Divisão inteira é {} e Potência é {}\n'.format(di, e))

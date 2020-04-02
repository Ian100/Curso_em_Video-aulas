print('\033[0;30;41mTeste\033[m')
print('\033[4;33;46mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')

nome = str(input('Digite seu nome: '))
print('Muito prazer, \033[1;31m{}\033[m!!!'.format(nome))

print('Muito prazer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'padrão':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto/branco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer {}{}{}!!'.format(cores['preto/branco'], nome, cores['padrão']))

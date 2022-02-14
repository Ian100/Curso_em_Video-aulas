nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome in 'Ana Cláudia Maria Andressa Juliana Paula':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Pedro Gabriel João':
    print('Que nome mais normal!')
print('Tenha um bom dia, {}!'.format(nome))

# Interactive Help
#
# Basta digitar o comando 'help()' sem as aspas, no console
# do python, depois execute o programa e você entrará
# na tela de Ajuda Interativa do Python. Você também pode
# digitar 'help(função())' ou 'print(função.__doc__)'
# dentro do IDE, sem as aspas. Depois basta digitar algum
# comando, biblioteca, função ou método que o python lhe
# mostrará todas as respectivas informações. Para sair da
# Ajuda Interativa, basta digitar 'quit', sem as aspas.

# Docstrings
#
# Logo após o 'def func()' - exemplo -, na linha abaixo digite
# aspas duplas três vezes.
# Ex:
#     def contador(i, f, p):
#         """
#         -> Faz uma contagem e mostra na tela.
#         :param i: início da contagem
#         :param f: fim da contagem
#         :param p: intervalo da contagem
#         :return: sem retorno
#         """
#         c = 1
#         while c <= f:
#             print(f'{c} ', end='')
#             c += p
#         print('FIM!')
#
#
#     help(contador)

# Parâmetros Opcionais
#
# Normalmente em Python quando se define uma função com
# parâmetros, espera-se que todos estes parâmetros sejam
# preenchidos/cumpridos, caso contrário, uma mensagem
# de erro será apresentada na tela. Mas, com o
# conceito de Parâmetros Opcionais, podemos alterar isso.
#
# Ex:
#    def soma(a, b, c):
#        s = a + b + c
#        print(f'A soma vale {s}')
#
#
#    soma(3, 2, 5)
#    soma(8, 4)
#    soma()
#
# Obs.: Nesta situação teríamos uma mensagem de erro
# na tela por não ter especificado todos os parâmetros
# dentro da função 'soma'.
#
# Agora aplicando o conceito de Parâmetros Opcionais à esta
# mesma função ficaria assim:
#
# def soma(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# soma(3, 2, 5)
# soma(8, 4)
# soma()
#
# Obs.: Note que atribuímos o valor 0(Zero) aos parâmetros
# 'a', 'b' e 'c'. Isso significa que caso não for informado
# NENHUM VALOR para qualquer um destes parâmetros,
# por PADRÃO eles valerão 0(Zero).

# Escopo de Variáveis
#
# Ex:
#    def teste(b):    - Escopo Local
#        a = 8
#        b += 4
#        c = 2
#        print(f'A dentro vale {a}')
#        print(f'B dentro vale {b}')
#        print(f'C dentro vale {c}')
#
#    a = 5            - Escopo Global
#    teste(a)
#    print(f'A fora vale {a}')
#
# Obs.: É possível mostrar na tela uma variável Global
# dentro de um Escopo Local, porém não é possível mostrar
# uma variável Local dentro de um Escopo Global.
#
# Obs.: No exemplo acima, a variável 'a' criada dentro do
# Escopo Local NÃO REPRESENTA a variável Global 'a'. Ao invés
# disso, quando definimos a variável Local 'a' com valor 8 no
# Escopo Local, foi criado na memória mais uma variável 'a'
# além da variável Global, sendo ao total duas variáveis,
# uma Local e outra Global.
#
# Ex:
#    def teste(b):     - Escopo Local
#        global a
#        a = 8
#        b += 4
#        c = 2
#        print(f'A dentro vale {a}')
#        print(f'B dentro vale {b}')
#        print(f'C dentro vale {c}')
#
#
#    a = 5             - Escopo Global
#    teste(a)
#    print(f'A fora vale {a}')
#
# Obs.: Note que no Escopo Local, logo abaixo do comando
# 'DEF', está escrito "global a". Esta palavra reservada
# chamada 'global', indica ao nosso programa que não queremos
# que ele crie uma nova variável 'a'(Local), mas ao invés
# disso use a variável Global 'a' dentro do Escopo Local.
# Assim 'a' Global passa a valer 8 tanto no Escopo Local
# quanto no Escopo Global.

# Retorno de Valores
#
# Ex:
#    def somar(a=0, b=0, c=0):
#        s = a + b + c
#        print(f'A soma vale {s}')
#
#
#    somar(2, 3, 5)
#    somar(2, 2)
#    somar(6)
#
# Obs.: No exemplo acima, note que não é possível personalizar
# o resultado, como no exemplo de baixo. Compare-os!
#
# Ex:
#    def somar(a=0, b=0, c=0):
#        s = a + b + c
#        return s
#
#
#    r1 = somar(3, 2, 5)
#    r2 = somar(1, 7)
#    r3 = somar(4)
#    print(f'Meus cálculos foram {r1}, {r2} e {r3}.')
#
# Obs.: Neste exemplo temos a palavra reservada 'return', que,
# neste caso, está retornando o valor da variável 's'.
# Sendo assim, é possível personalizar a forma como queremos
# que o resultado da função 'somar' apareça na tela.

# Parte Prática:

def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(numb=0):
    if numb % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número inteiro: '))
if par(num):
    print('Este número é PAR')
else:
    print('Este número é ÍMPAR')

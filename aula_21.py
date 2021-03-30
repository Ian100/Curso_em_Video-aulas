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

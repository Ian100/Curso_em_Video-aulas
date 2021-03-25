# Hoje trabalharemos com FUNÇÕES!
#
# TODA FUNÇÃO VEM ACOMPANHADA DE PARÊNTESES!
# Ex: print()
#
# Para criar uma função personalizada usa-se o comando DEF!
# Ex: def nome_da_nova_função():
#           Aqui vai o código da nova função!
# Ex:       print('Olá, Mundo!')

# Função sem Parâmetro:
def lin():
    print('-' * 30)


# Função com Parâmetro:
def título(txt):
    lin()
    print(f'{txt:^30}')
    lin()


# EMPACOTAMENTO E DESEMPACOTAMENTO DE PARÂMETROS:
#
# A maioria das linguagens de programação
# não permitem a contagem de parâmetros dentro de uma mesma função!
# O Python permite! Isso é chamado de EMPACOTAMENTO!
# Ex:
#    def contador(* núm):
#        _ Aqui vai o seu código! _
#
#    Obs.: O '*' é o símbolo para desempacotar,
#          ou seja, ele está dizendo ao python
#          para jogar todos os parâmetros do usuário
#          na variável núm, sejam eles quais forem.
def contador(* núm):
    tam = len(núm)
    print(f'Para os números {núm} existem {tam} valores.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal 1
lin()
print(f'{"CURSO EM VÍDEO":^30}')
lin()
print(f'{"APRENDENDO PYTHON":^30}')
lin()
print(f'{"GUSTAVO GUANABARA":^30}')
lin()

# Programa Principal 2
título('CURSO EM VÍDEO')
título('APRENDA PYTHON')
título('GUSTAVO GUANABARA')

# Programa Principal 3
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Programa Principal 4
valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)

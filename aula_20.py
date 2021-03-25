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

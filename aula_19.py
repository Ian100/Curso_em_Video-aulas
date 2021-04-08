# HOJE FALAREMOS SOBRE DICIONÁRIOS!
#
# RECAPITULANDO:
#
# dado = list()
# dado.append('Pedro')
# dado.append(25)
# print(dado[0])   Pedro
# print(dado[1])   25
# ---------------------------------
# - - - - -- DICIONÁRIOS -- - - - -
#
# Os Dicionários são identificados
# pelas chaves "{" e "}".
# Exemplos:
#
# dado = dict()
# dado = {}
# --------------------------
# dado = {'nome':'Pedro', 'idade':25}
# print(dado['nome'])  Pedro
# print(dado['idade']) 25
# ---------------------------------------------------
# Quando se quer adicionar um novo elemento
# a um dicionário, basta fazer assim:
#
# dado['novo_elemento'] = 'valor_do_novo_elemento'
# ---------------------------------------------------
# dado['sexo'] = 'M'
# ---------------------------------------------------
# Para deletar um dicionário ou
# um elemento de um dicionário, basta
# usar o comando del que foi visto nas
# aulas anteriores.
# Exemplo:
#
# del dado['nome_do_elemento']
# ---------------------------------------------------
# del dado['idade']
# ---------------------------------------------------
# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'
#         }
# print(filme.values()) Mostra os Valores do dicionário "filme"
# print(filme.keys()) Mostra as Chaves do dicionário "filme"
# print(filme.items()) Mostra os Itens do dicionário "filme"
# for k, v in filme.items():
#     print(f'O {k} é {v}')      O titulo é Star Wars
#                                O ano é 1977
#                                O diretor é George Lucas

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]}, do sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos.')
print('----------------------------------------------------------------')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('----------------------------------------------------------------')
# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('----------------------------------------------------------------')
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
del brasil
print('----------------------------------------------------------------')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip()
    brasil.append(estado.copy())  # Copia todos os elementos do
for e in brasil:                  # dicionário estado para a lista
    for k, v in e.items():        # brasil
        print(f'O campo {k} tem valor {v}')
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

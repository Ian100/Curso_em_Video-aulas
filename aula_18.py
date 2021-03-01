# LISTAS Parte 2
#
# [Lista]
# [[Lista dentro de uma lista]]
#
# dados = list()
# dados.append('Pedro')
# dados.append(25)
# print(dados[0]) Pedro
# print(dados[1]) 25
#
# pessoas = list()
# pessoas.append(dados[:])
# pessoas.append('Maria')
# pessoas.append(19)
# pessoas.append('João')
# pessoas.append(32)
#
# print(pessoas[0][0]) Pedro
# print(pessoas[1][1]) 19
# print(pessoas[2][0]) João
# print(pessoas[1]) ['Maria', 19]

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totM = totm = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totM += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totm += 1

print(f'Temos {totM} maiores e {totm} menores de idade.')

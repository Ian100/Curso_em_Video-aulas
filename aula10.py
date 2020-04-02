# n = str(input('Digite seu nome: '))
# if n == 'Gustavo':
    # print('Que nome lindo você tem!')
# else:
    # print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(n))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi de {} pontos!'.format(m))
if m < 7:
    print('Você tirou uma média muito baixa!\nESTUDE MAIS!')
if m == 7:
    print('Você passou raspando!\nPrescisa estudar mais!')
if m > 7:
    print('PARABÉNS! Sua nota está ótima!\nContinue sempre assim!')

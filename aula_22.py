# Módulos e Pacotes
#
# Modularização:
#
# - Surgiu no início da década de 60
# - Sistemas ficando cada vez maiores
# - Foco: dividir um programa grande
# - Foco: aumentar a legibilidade
# - Foco: facilitar a manutenção

import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatprial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')

# Obs.: Note que, dentro desta mesma pasta foi criado um arquivo
# chamado uteis. Neste arquivo, nós armazenamos todas as funções
# utilizadas neste programa, e o fizemos não só para facilitar
# a manutenção futura, como também para aumentar a legibilidade
# do arquivo.

# Obs.: No Python, todo arquivo .py pode ser um módulo contanto
#  que ele tenha funções internas, como em 'uteis.py'.
#  Este é o conceito da Modularização!

# Vantagens da Modularização:
#
# - Organização do código
# - Facilidade na manutenção
# - Ocultação de código detalhado
# - Reutilização em outros projetos
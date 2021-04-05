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

# Pacotes:
#
# Um Pacote nada mais é do que a junção de módulos separados
# por assunto dentro de uma ou várias pastas. Pacotes normalmente
# são usados quando um módulo fica extremamente grande e complexo,
# sendo de difícil entendimento e organização.
#
# Para criarmos um Pacote, primeiro precisamos entender algumas coisas:
#
# - Todo arquivo .py pode ser potencialmente um módulo.
# - Dentro de um projeto Python, TODA PASTA é CONSIDERADA um PACOTE!
#
# Então, se dentro do projeto tivermos um Pacote chamado uteis, basta
# criarmos uma pasta chamada uteis, e se dentro deste Pacote tivermos
# vários módulos, basta criar várias pastas com os seus respectivos nomes.
# Depois apenas basta importá-la(as pastas com o Pacote e eventualmente
# com os respectivos módulos) para dentro do seu programa principal.

# Tratamento de ERROS e Exceções

# Quando um ERRO não se dá de forma sintática, ele é chamado de Exceção!
# Ex: primt('Olá') - Erro Sintático
#     print(x) - Exceção NameError (pois a variável X não existe)

# Toda Exceção no Python é filha de uma classe maior chamada Exception.
# Sempre que nós virmos na tela a palavra Exception, a leremos como
# Exceção.
# Para tratarmos uma Exceção em Python temos um comando bem específico
# chamado 'try' e outro chamado 'except'. Se o código dentro do comando
# 'try' resultar em uma Exceção, o comando 'except' é executado!
# Ex:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'Problema: {erro.__class__}')

# No caso de o camando 'try' não resultar em uma Exceção, nós temos o
# comando 'else', que, no caso de 'try' não ter recebido Exceção alguma,
# é executado imediatamente!
# Ex:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'Problema: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')

# E ainda temos uma última cláusula ou comando chamado 'finally', que
# será executada independente se o comando 'try' tenha recebido uma
# Exceção ou não, SEMPRE!
# Ex:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'Problema: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('\nVolte sempre! Muito obrigado!')

# Obs.: As cláusulas 'else' e 'finally' são opcionais, isso significa
# que nem sempre nós precisamos usa-las.

# Obs.: Todo comando 'try' pode ter vários comandos 'except'.
# Ex:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('\nO usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('\nVolte sempre! Muito obrigado!')

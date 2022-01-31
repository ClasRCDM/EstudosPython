print('{1}{0}{2}{3}'.format(f'{"_ Aula 23 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

try:  # Operação
    a = int(input('Numerador: '))
    b = int(input('Dominador: '))
    r = a / b
except (ValueError, TypeError):  # Falha
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:  # Falha
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:  # Falha
    print('O usuário preferiu não informar os dados!')
except Exception as error:  # Falha
    print(f'O erro foi: {error.__class__}')
else:  # Deu certo
    print(f'O resultado é {r:.1f}')
finally:  # Independente do resultado
    print('Volte sempre! Muito obrigado!')

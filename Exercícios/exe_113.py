print('{1}{0}{2}'.format(f'{"_ Exercício 113 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))


def leiaInt(msg):
    while True:
        try: n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt: 
            return 0, print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        else: return n, print(end='')


def leiaFloat(msg):
    while True:
        try: n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt: 
            return 0, print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        else: return n, print(end='')


# - 

num = leiaInt('Digite um Inteiro: ')[0]
num2 = leiaFloat('Digite um Real: ')[0]
print(f'O valor inteiro digitado foi {num} e o real {num2}.')

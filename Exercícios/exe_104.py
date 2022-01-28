print('{1}{0}{2}{3}'.format(f'{"_ Exercício 104 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else: print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok: break
    return valor


# -

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

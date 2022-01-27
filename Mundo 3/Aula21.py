print('{1}{0}{2}{3}'.format(f'{"_ Aula 21 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

# Interactive HELP
help(print)
print(input.__doc__)
print('\n')


# DOCSSTRINGS
def contador(i, f, p):  # Parametros real
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10, 2)  # Parametros formal
help(contador)


# Parâmetros Opcionais
def somar(a=0, b=0, c=0):  # Parametros real
    s = a + b + c
    print(f'A soma vale {s}' if s != 0 else f'Você não informou nenhum número.')


somar(3, 2, 5)  # Parametros formal
somar(8, 4)  # Parametros formal
somar()  # Parametros formal
print('-=' * 15)


# Escopo de variáveis
def teste():
    global a  # Transforma o a local no a global
    a = 2  # Variável local
    x = 8  # Variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2  # Variável global
a = 5  # Variável global
print(f'No programa principal, n vale {n}')
teste()
print(f'O a que valia 5 agora vale {a}')
print('-=' * 15)


# Retornado valores
def somar2(a=0, b=0, c=0):
    return a + b + c


print(somar2(3, 2, 5))
print(somar2(2, 2))
print(somar2(6))

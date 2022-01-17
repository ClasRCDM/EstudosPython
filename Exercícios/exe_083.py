print('{1}{0}{2}{3}'.format(f'{"_ Exercício 83 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

expr = str(input('Digite a expressão: '))
lista = list()

for simb in expr:
    if simb == '(': lista.append('(')
    elif simb == ')':
        if len(lista) > 0: lista.pop()
        else:
            lista.append(')')
            break
else: print('Sua expressão está válida!'
            if len(lista) == 0 else
            'Sua expressão está errada!!')

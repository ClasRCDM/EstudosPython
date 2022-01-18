print('{1}{0}{2}{3}'.format(f'{"_ Exercício 89 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

while True:
    nome = str(input('Nome: '))

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    if str(input('Quer continuar? ')).strip()[0] in 'Nn': break
print('{1}{2}{0}{2}{1}'.format(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}', '-=' * 15, '\n'))

# for i, a in enumerate(lista): print(f'{i:<4}{a[0]:<5}{a[2]:>8.1f}')
[print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') for i, a in enumerate(lista)]

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    elif opc <= len(lista) - 1: print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
else: print('<<< VOLTE SEMPRE >>>')

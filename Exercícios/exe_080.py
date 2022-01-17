print('{1}{0}{2}{3}'.format(f'{"_ Exercício 79 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

for pos in range(5):
    valor = int(input('Digite um valor: '))
    if pos == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posi = 0
        while posi < len(lista):
            if valor <= lista[posi]:
                lista.insert(posi, valor)
                print(f'Adicionado na posição {posi}°')
                break
            posi += 1

print(lista)

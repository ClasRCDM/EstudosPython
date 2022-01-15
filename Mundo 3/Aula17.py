print('{1}{0}{2}{3}'.format(f'{"_ Aula 17 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

num = [2, 5, 7, 1]
num[2] = 44
num.append(66)
num_ordenado = sorted(num)
num.insert(2, 0)

print(num)
print(num_ordenado)

print(f'Esta lista tem {len(num)} elementos')
num.pop()
print(num)

valores = list()

for v in range(5, 0, -1):
    valores.append(v)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
else:
    print('Cheguei ao final da lista.')

valores2 = valores[:]  # Cria uma copia dos valores
valores3 = valores  # Liga duas listas, onde se mudar uma a outra muda junto

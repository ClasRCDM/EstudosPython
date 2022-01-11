print('{1}{0}{2}'.format(f'{" Aula 15 ":=^25}', '\033[4;33m', '\033[m'))

cont = 1
while True:
    print(f'{cont} ->', end=' ')
    cont += 1
    if cont >= 20:
        break
    if cont >= 10:
        continue
else:
    print('oi')
print('oi break')

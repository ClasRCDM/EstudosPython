from time import sleep

print('{1}{0} Desafio 46 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

for fogos in range(0, 10):
    print('{}{}{}'.format('\033[4;35m', fogos, '\033[m'))
    sleep(1)
else:
    print('{}BUM!!! FOGOS DE ARTIFICIO{}'.format('\033[4;31m', '\033[m'))

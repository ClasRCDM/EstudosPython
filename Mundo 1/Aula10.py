print('{0} Aula 10 {0}'.format('=' * 10))

nome = str(input('Qual o seu nome: ')).strip()

if nome.title() in ['Raphael', 'Gustavo', 'Deus']:
    print('Que nome lindo você tem!')
else:
    print('Nada demais seu nome')

print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A sua média foi {:.2f}'.format(m))

if m >= 6.0:
    print('Sua média foi BOA')
else:
    print('Sua nota foi ruim')

print('{0} Desafio 31 {0}'.format('=' * 10))

distancia = float(input('Distancia da viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('O preço da viagem vai ser {}'.format(valor))

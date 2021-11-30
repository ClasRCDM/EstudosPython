print('{0} Desafio 31 {0}'.format('=' * 10))

distancia = float(input('Distancia da viagem: '))

print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

'''if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45'''

valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('O preço da viagem vai ser R${:.2f}'.format(valor))

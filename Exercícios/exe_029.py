print('{0} Desafio 29 {0}'.format('=' * 10))

velocidade = float(input('Velocidade do carro: '))

if velocidade > 80:
    v = (velocidade - 80) * 7

    print('Você excedeu o limite permitido de 80Km/h')
    print('Você foi mutado OTARIOO!!!\nVocê ira pagar R${:.2f}'.format(v))
else:
    print('Segui uma boa viagem')

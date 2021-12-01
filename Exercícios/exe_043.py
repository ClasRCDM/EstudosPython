print('{1}{0} Desafio 43 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

peso = float(input(('QUal é o seu peso? (Kg) ')))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA!!. sua vida esta em risco...')

print('{1}{0} Desafio 44 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))
total = 0

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2

    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco
    total = total + (preco * 20 / 100)

    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc

    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('OPÇÃO INVALIDA de pagamento. Tente novamente')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

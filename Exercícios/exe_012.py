print('{0} Desafio 12 {0}'.format('=' * 10))
preco = float(input('Preço do produto? '))
cal = preco * 5/100 - preco
print('Com 5% de desconto, o preço fica R${} reais'.format(cal*-1))

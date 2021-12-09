print('{1}{0} Desafio 56 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

somaidade = 0
médiaidade = 0

maioridadehomen = 0
nomevelho = ''

totmulher20 = 0

for p in range(1, 5):
    print('----- {} PESSOA ------'.format(p))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    somaidade += idade

    if p == 1 and sexo in 'M':
        maioridadehomen = idade
        nomevelho = nome
    elif sexo in 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    elif sexo in 'F' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4

print('A média de idade do  grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

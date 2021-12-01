print('{1}{0} Desafio 40 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

nota1 = float(input('Primeira nota: \033[32m'))
nota2 = float(input('\033[mSegunda nota: \033[32m'))

nota_final = (nota1 + nota2) / 2

print('\033[34mSua nota é {}'.format(nota_final))

if nota_final < 5:
    print('\033[31mVocê esta REPROVADO!!!')
elif 5 >= nota_final <= 6.9:
    print('\033[33mVocê entrou em recuperação!')
else:
    print('\033[30mVocê foi APROVADO!!!!!!')

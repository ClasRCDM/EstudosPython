print('{0} Desafio 11 {0}'.format('=' * 10))
lar = float(input('Largura: '))
alt = float(input('Altura:  '))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(
    lar, alt, area))
print('Para pintar essa parede, precisa de {:.2f}L de tinta'.format(
    area / 2))

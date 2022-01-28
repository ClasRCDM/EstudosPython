print('{1}{0}{2}{3}'.format(f'{"_ Exercício 105 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vários informações sobre a situação da turma.
    """
    
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7: r['situação'] = 'BOA'
        elif r['média'] >= 5: r['situação'] = 'RAZOÁVEL'
        else: r['situação'] = 'RUIM'
    return r


# -

resp = notas(5.5, 2.5, 9, 8.6)
resp2 = notas(5.5, 2.5, 9, 8.6, sit=True)
print(resp)
print(resp2)

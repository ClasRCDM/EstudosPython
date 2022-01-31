import urllib
import urllib.request

print('{1}{0}{2}'.format(f'{"_ Exercício 114 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

try: site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError: print('\033[31mO site Pudim não está acessível no momento.\033[m')
else: print('\033[32mFoi possível acessar o site Pudim.\033[m')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def minhafunc(self):
        print(f'Ola meu nome é {self.nome}')


p1 = Pessoa('Eduarda', 19)

print(p1.nome)
print(p1.idade)
p1.minhafunc()

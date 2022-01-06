from datetime import datetime
from typing_extensions import runtime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        # Variáveis dentro da instância
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, comendo):
        print(f'{self.nome} está comendo... {comendo}')
        self.comendo = True

    def falar(self, fala):  # Método da Classe
        if self.falando:
            print(f'{self.nome} já está falando...')
            return

        print(f'{self.nome} está falando... {fala}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} já paro de falar...')
            return  # return sozinho, sai do método

        print(f'{self.nome} não está falando...')
        self.falando = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

from pessoa import Pessoa

# p1 = Pessoa('Marcos', 45)
p1 = Pessoa.por_ano_nascimento('Marcos', 1977)

print(p1.ano_atual)

print(p1.idade)
p1.get_ano_nascimento()

# Métodos Mágicos (Magic Methods, dunder methods(double underscore))
class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['Habilidade ', 'Habilidade 2', 'Habilidade 3']
    
    # Representação para programadores(chamado com método repr(pessoa))
    def __repr__(self):
        return 'Classe Pessoa com propriedades nome e habilidades'
    
    # O que deve ser mensurado para determinar a quantidade daquela classe(chamada com método(len(pessoa)))
    def __len__(self):
        # len(pessoa) ?
        return len(self.habilidades)

    def __str__(self):
        return f'{self.nome} com as habillidades {self.habilidades}'


pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))
# Polimorfismo
class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Lignado a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)


class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)

pessoa = Pessoa()
pessoa.apresentar(nome='Amanda', idade=18, profissao='Programadora')
pessoa.apresentar(nome='Amanda', idade=18)
pessoa.apresentar(nome='Amanda', profissao='Programadora')
pessoa.apresentar(nome='Amanda')
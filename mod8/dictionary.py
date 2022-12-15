# Dictionary compreheension # 'dicionarios apartir dessa estrutura'
# [expressão for membro in iterável]
# {chave:expressao for mebro in interável}
from pprint import pprint
pprint({exemplo: exemplo for exemplo in range(20)})
# Popular um dicionário com valores
produtos = ['produto1', 'produto2', 'produto3', 'produto4','produto5']
pprint({produto: 1 for produto in produtos})
# Gerar uma matriz de valores de teste
pprint({produto: [0 for i in range(5)] for produto in produtos})
# [expressão for membro in iterável]
pprint({produto: [i*2 for i in range(5)] for produto in produtos})
# Gerar valores de teste usando o random
import random
pprint({produto: [random.randint(1000, 15000) for i in range(5)] for produto in produtos})


# Desafio 1

sorteios = [' Sorteio 1', ' Sorteio 2', ' Sorteio 3']
participantes = ['joel', 'jessica', 'maria', 'cris', 'larissa', 'rafael', 'marcus', ' john']
pprint({sorteio: random.choice(participantes) for sorteio in sorteios})

# Desafio 2

grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3']
pprint({grupo: [random.randint(1, 100) for i in range(5)] for grupo in grupos})


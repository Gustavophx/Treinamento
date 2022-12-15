# Como podemos cirar listas?
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# MAP
nomes = ['Larissa', 'rafael', 'marcus', 'john']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'
map(aprovar_pessoa,nomes)
print(list(map(aprovar_pessoa,nomes)))# pra exibir o resultado de forma clara, use a função list antes do map


# Como usar uma list compreheension
nova_lista = [2 * ex for ex in range(10)]
print(nova_lista)
nomes = ['Larissa', 'rafael', 'marcus', 'john']
print([nome + ' APROVADO' for nome in nomes])
print([aprovar_pessoa(nome) for nome in nomes])

""" 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""
from pprint import pprint
pprint([[i for i in range(1,6)] for loop in range (5)]) # Range nunca gera o ultimo valor

# Usar condicionais em list compreheension
#  [expressao for membro in iterável (condicional if)]
nomes = ['Larissa', 'rafael', 'marcus', 'john']
print([aprovar_pessoa(nome) for nome in nomes if nome != 'rafael'])
# Valores numéricos
def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False

print([ex for ex in range(20) if eh_numero_par(ex)])

# A condicional é flexível
# [expressao (condicional if) for membro in iterável]
""" participantes = ['Larissa', 'rafael', 'marcus', 'john']
ganhadores = ['marcus', 'john']
print([ex + ' GANHADOR' if ex in ganhadores else ex + ' NÂO SELECIONADO' for ex in participantes])
 """

# Desafios
# 1
print([i*2 for i in range(1,6)])


# 2
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
pprint([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

# 3
participantes = ['joel', 'jessica', 'maria', 'cris', 'larissa', 'rafael', 'marcus', 'john']
pagamento_realizado = ['joel', 'jessica', 'maria', 'cris']

print([ex + ' Pago' if ex in pagamento_realizado else ex + ' Devendo' for ex in participantes])
# Como podemos criar listas?

# Criar listasl usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']


def aprovar_pessoa(nome):
    return nome + ' Aprovado'


print(list(map(aprovar_pessoa, nomes)))


''' DESAFIO -

# ExtraiA as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.'''

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

cores = []
for cor in pinturas:
    cores.append(cor[1])

print(cores)

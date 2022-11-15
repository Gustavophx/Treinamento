# Enumerate
for indice, numero in enumerate(range(1, 11),1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for indice, nome in enumerate(nomes,1):
    print(indice, nome)
    if indice == 3:
        print('Ja temos 3 pessoas registradas')

# Desafio 1
'''
Itere sobre a lista abaixo exibindo o número do índice + nome da fruta. Porém quando o índice for 3 exiba 'Nº índice + nome da fruta EM PROMOÇÂO'
frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
'''

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice, fruta in enumerate(frutas,0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÂO')
    else:
        print(indice, fruta)
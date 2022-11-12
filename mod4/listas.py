# Listas
precos = [10,20,30]

print(precos[2]) # Acessar a lista por índice, OBS no Python sempre se inicia do 0, a não ser que use algo pra iniciar do 1.

print(precos[precos.index(10)])# Como descobrir o valor ou algo da lista apenas com a informação/valor utilizer o '.index()' (EX)

# Listas no python são dinãmicas(aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista
# Multiplicação devalotes(repetição)
lista_de_noves = [9] * 10
lista_de_testes = ['Teste'] * 10 # Basicamente o que esta entre [] e considerado uma lista.
print(lista_de_noves)
print(lista_de_testes)

# Usando gerador Range(sequência)
# 1 ate 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)
# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))# cada letra do 'string' fica de forma separada e vira uma lista.
# Lista de lista(matriz)
matriz_de_nomes = [['Carol',30], ['Marcus',60]]
print(matriz_de_nomes[0]) # acessa a index em geral []
print(matriz_de_nomes[0][0]) # acessa a index dentro da [] e se tiver varias informações o proximo [] pegarar a camada referente a ela por isso [][]
print(matriz_de_nomes[1][0])

# Desafios 🥇

''' 

Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela

Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131

Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2

Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos

 que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 

uma informação extra, coloque o valor em reais desse objeto também e imprima ele 

na tela  

'''

objetos = ['celular', 'chaves', 'carteira']
print(objetos)

numeros = list(range(10, 132))
print(numeros)

print(objetos + numeros)

matriz_de_objetos = [['celular', 'preto', 1500], ['chaves', 'casa', 5], ['carteira', 'couro', 30]]
print(matriz_de_objetos[1][2])
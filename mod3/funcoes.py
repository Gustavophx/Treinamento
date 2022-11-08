#funçôes
# input() # (receber dados do usuario)
# len() # (tamanho de um objeto)
# split() # (transforma string em listas)
'''
def nome_da_funcao(parametros):
    comandos
'''
def dar_boas_vindas(): #def funciona como dar função
    print('Bem-vindo! ')

dar_boas_vindas()

def dar_boas_vindas_personalizada(nome):
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personalizada('Gustavo')

# Valor padrão
def apresentar_lugar(horario_de_funcionamento,lugar='nossa loja'):
    print(f'Conheça {lugar}, horário de funcionento das {horario_de_funcionamento}')

apresentar_lugar('08:00 as 18:00')




# Desafio🥇

'''

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade,
# porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

'''

# Desafio 1
def gerar_nome_completo(nome, sobrenome):
    print(f'{nome} {sobrenome}')

gerar_nome_completo('Gustavo', 'Olivera')

# Desafio 2

def calcular_valores(preco, quantidade=1):
    print(preco*quantidade)

calcular_valores(10, 2)
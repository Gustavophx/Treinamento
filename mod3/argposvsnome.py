# Argumentos possicionais VS Argumentos nomeados

def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} esta no valor de: {preco}') # usando F dentro das ()e factorial ou ira usar {}pra combinar com outras {} na frase a ser exibida.

# Argumentos posicionais (a informação que sera exibida estara na forma que foi escrita no codigo)
exibir_preco(5000,'Iphone')

# Argumento nomeados, a informação/ argumento estarar corretar mesmo em locais diferente pois estarar seguida do variavel(=)'Ex' 
exibir_preco(preco=5000, nome_produto='Iphone') # variaveis invertina, mas na exibição estaram correta pelo nomeamento do argumento.

# Forma de coloca o codigo no Argumento nomeado e adicionando um * no codigo 'def' depois da virgula, irar obrigar usar a função que o dev definiu.
# Ex nome_produto e preco, em vez de so o nome e valor.


# Desafio 🥇

'''
Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:
1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
'''

def gerar_objeto_personalizado(cor,*,altura, formato): # se quiser obrigar o nomeamento lembrar de usar [,*,]
    print(cor, altura, formato)

gerar_objeto_personalizado('azul', altura=1.50, formato='Quadrado')

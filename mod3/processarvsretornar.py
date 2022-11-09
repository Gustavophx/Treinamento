# Processar VS Retornar
# Função que apenas processa dados
print('Olá!') # Processar, comando interno pra mostrar a informação

# Funções que retorna dados
cidade = input('Qual é a sua cidade?') # Input e usado pro usuario nos da a informação, e podemos guardar essa informação em uma variavel.(Cidade)

# Como escolher entre funções que processam VS retornam dados?
''' Eu vou precisar de uasr essa informação na lógica do meu programa ainda? ou só preciso processar esse dado,
 mais não irei utilizar mais ele depois?'''
def exibir_cotacao_do_dia(moeda):  #(def usado pra criar uma função que pode ser usada mais tarde)
    if moeda == 'usd': # [if] funciona como 'caso seja'
        print(5.47)

exibir_cotacao_do_dia('usd') 

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47 # (return e usada como informação pra ser usada mais tarde basicamente)

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em ações americanas')
else:  #[else se a informção não bater com o IF ou else = "caso contrario"]
    print('Cotação não favorável')
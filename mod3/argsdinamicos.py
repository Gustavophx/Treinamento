# Args - Funções com nº de argumentos dinâmicos
'''
def somar(valor, b): 
    print(valor + b)

somar(5, 5)'''

def somar(*valores, b):#para adicionar mais valores, use a * na primeira informação,e lembrar de colocar no plural
    print(valores)
    for valor in valores:# de forma rapidar usar um "laço"  "[for] valor [in]"
        b += valor
    print(b)



somar(10,20,5 , b=5)# dessa forma o ultimo argumento deve ser nomeado, ex 'b='
# *args(variavel de argumentos para aquele paramentro)(varias informações)

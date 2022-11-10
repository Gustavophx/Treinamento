# Decorators
'''
def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1

resultado = pai(1)
resultado()'''

def meu_decorator(funcao):
    def wrapper(): # 'Wrapper e apenas exemplo pode ser qualguer nome pra função
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns !!!')

parabenizar()
'''
resultado = meu_decorator(parabenizar)# usando @meu_decorator daria pra simplificar o codigo encurtando essas 2 linhas 27 e 28
resultado()
'''

# Desafio🥇
# Crie um decorador que irá pegar a função que for passado para ele e imprimir o horário atual antes de executar a função
# e depois imprimir o horário após finaliazdo a execução da função
# ° Dica: você terá que usar o módulo datetime para conseguir o horário atual

from datetime import datetime

def monitorar_horario(funcao): # criando a estruturar pra ser usado mais tarde
    def horario():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return horario

@monitorar_horario # Utilizando a estrutura criada anteriormente
def baixar_musicas():
    print('Baixando músicas')

baixar_musicas()


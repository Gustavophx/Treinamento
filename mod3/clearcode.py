# Clear code - na prática
from turtle import Turtle

t = Turtle()

def obter_distancia():
    resposta = int(input('Quantos pixels devemos movimentar para a frente? '))
    return resposta

def rotacionar_turtle(turtle):
    movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:não rotacionar')
    if movimentar_para_lado == 'd':
        rotacionar_para_direita(turtle)
    elif movimentar_para_lado == 'f':
        rotacionar_para_esquerda(turtle)

def rotacionar_para_direita(turtle):
    angulo = int(input('Quanto para a direita devemos rotacionar?'))
    t.right(angulo)

def rotacionar_para_esquerda(turtle):
    angulo = int(input('Quanto para a esquerda devemos rotacionar?'))
    t.left(angulo)

while True:
    direcao = input('Para qual direcao devemos ir? "f:frente" ou "t:trás"')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break
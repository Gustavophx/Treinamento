'''
# Desafio 🥇

### Desafio 1 
Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás)
 e qual ângulo deverá ser tomado a cada nova movimentação

### Desafio 2 
Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário

#### Dicas Iniciais
* Crie uma nova turtle primeiro
* Coloca seu programa em loop 
* Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás
* Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos
* Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta
* Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados
* Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

#### Dicas Adicionais
* Não esqueça de converter o input do usuário para o tipo apropriado
* Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 
Pergunte -> Processe resposta -> Aja de acordo com a resposta -> Pergunte se deve continuar -> repita(se necessário)
'''

from turtle import Turtle
# Inicializando um turtle
t = Turtle()
# definindo uma velocidade
t.speed(1)
while True:
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás"')
    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:não rotacionar')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar?'))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar?'))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(input('Quantos pixeis devemos movimentar para a trás? '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerdar n:não rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quantos para a direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quantos para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continmuar andando? ')
    if resposta not in ('sim', 's'):
        break



import time
velocidade_internet = 10
print(velocidade_internet)
# Números = (INT)
velocidade_intenet = 10  # números

# Valores boleanos (BOOL)
esta_aberta = True  # true ou false

# Stirngs (STR)
slogan = 'Feito é melhor que perfeito'  # Texto
# pode usar ' ou " mas não pode misturar
slogan = "Feito é melhor que perfeito"
# guardando informação referente a coluna do lado de forma mais facil e rapido " X = X "
a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)
print(type(a))  # como saber o tipo da variavel
print(type(velocidade_internet))

# desafio
variavel_1 = 25.87
variavel_2 = True
variavel_3 = 'Bom dia!'
variavel_4 = 15

# Resposta
print(type(variavel_1))
print(type(variavel_2))
print(type(variavel_3))
print(type(variavel_4))


# 3 - Indentação
#  Desafio


def PensarPor10Segundos():
    print('pensando')
    time.sleep(10)
    print('Lembrei!')


if 10 > 5:
    print('10 é maior que 5')


class BemVindo():
    def __init__(self):
        print('Bem vindo')


oi = BemVindo()

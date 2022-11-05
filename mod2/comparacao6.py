# Aula - Operador ternário
# Caso a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade, caso contrário ela é menor de idade.
idade = 15
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# Outra forma de fazer comparação usando Operador ternário

idade = 25
print('Maior de idade') if idade >= 18 else print('Menor de idade')
# expressao / if / condicao (idade) / else / expressao

possui_passaporte = False
print('Favor embarcar') if possui_passaporte else print('Favor tirar passaporte')

# DESAFIO 🥇
# uso expressão condicional(operador ternário) para criar a seguinte condição
# se velocidade estiver acima de 100 exibir, você foi multado, caso contrário exiba siga em frente

velocidade = 80
print('Voce foi multado') if velocidade >= 100 else print('Siga em frente! ')
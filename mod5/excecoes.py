# Exceções
'''
try:
    valor = int(input('Digite um valor em dolares: '))
    print(valor * 5.25)
except:
    print('Favor digitar apenas números')
'''
try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um índice válido') # utilizado pro usuario não ver o erro
    print(erro) # caso precisamos ver o erro pra solucionar, nunca exibir para o usuario
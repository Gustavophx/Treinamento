# Conversão entre tipos
idade = input('Digite a sua idade ')# tudo no input e recebido como string, precisa converter caso precise trabalhar com numeros
print(int(idade) > 17) # converter com int(exemplo do input) ...

ano_publicacao = 2020
print('Este livro foi criado em ' + str(ano_publicacao))# e não podemos misturar str + int, precisamos fazer uma conversao.

altura = input('Altura da parede? ')
print(float(altura) > 2.50)# nesse caso precisou converter a altura em float, numeros com virgulas

# Conversões entre coleções
saudacao = 'Hello!'
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(30))) # Exemplo de conversão mais organizado em vez de numero por linha

numeros = [10, 20, 20, 50]
print(set(numeros)) # retira as duplicatas
print(tuple(numeros)) # vira uma lista imutavel
print(type(numeros)) # revela o formato de infomação da lista
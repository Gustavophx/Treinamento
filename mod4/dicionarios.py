# Dicionários

'''
Pessoa 
    nome
    idade
    altura
'''
pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]
# Dicionario
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura':1.60} # utilizando 'string' como chave do dicionario Ex = 'xx':'xx'
print(dicionario_pessoa)
pessoa_2 = dict(nome='Carol', idade=18, altura=1.60) # Outra forma de criar dicionario
print(pessoa_2)

print(pessoa_2['idade']) # Forma de acessar uma propriedade expecifica no dicionario.
print(dicionario_pessoa.keys()) # Forma de acessar todas as chaves disponiveis pra esse dicionario
print(dicionario_pessoa.values()) # Forma de acessar os valores de cada chave
print(dicionario_pessoa.items())# Forma de acessar tanto chave quanto valor 'tupla'
# iterar sobre um dicionario
for item in dicionario_pessoa.items():
    print(item[1])
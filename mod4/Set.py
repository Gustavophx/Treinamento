# SET
# Com a função Set não se repetem infomrações duplicadas.
numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}
# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Com a função Set e possivel adicioanr novos valores
set_numeros.add(10)
print(set_numeros)

# Conjuntos 
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3 ,9]
a = set(numeros1)
b = set(numeros2)
print(a.symmetric_difference(b)) # Função pra junta as diferenças da lista em uma só.
print(a.intersection(b)) # Função pra retorna o que esta igual na lista / valores em comum.
print(a.union(b)) # Função utilizada pra junta a lista, sem repetir informações repetidas.
# Tuplas. Obs: valores dentro da lista, não podem ser modificados.
site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'instagram.com'
# Ou
valor1 = 23 
valor2 = 43
valor3 = 65
# Criação de tupla
sites = ('youtube.com', 'facebook.com', 'instagram.com')# pode adicionar varias formas usando o tuplas, 'int','string','boleano'
valores = (23,43,65)
print(sites[1])
print(valores[2])
# União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)
# Acesso de valores em uma tupla
print(dados_do_sistema[2])

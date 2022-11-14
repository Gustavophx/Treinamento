# Manipulação de Listas
valores = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]
# Adicionar ao final da lista usamos o .append()
valores.append(11)
print(valores)
# Unir listas usando o .extend()
valores.extend(anos) # .extend não pode ser usada pra retorno ou pra criar uma nova lista ex nova_lista = valores.extend(anos)
print(valores)
# Adicionar lista
nova_lista = valores + anos
print(nova_lista)
# Inserir novo valor na lista
print(anos[1])
anos.insert(2, 2031)
print(anos)
# Extrair com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)
# Remover item da lista
anos.remove(2050)# Por valor
del anos[2]# Por index
print(anos)
del valores[1:7]# Faixa de valores apenas com del
print(valores)
# Contando a ocorrência de um valor (Quantas vezes ele aparece) .count
print(valores.count(2))
# Resetar (Deletar tudo da lista)
valores.clear()
print(valores)
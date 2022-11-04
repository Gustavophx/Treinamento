teclado = 'Teclado' # No python sempre começa conta pelo 0 espaço conta tambem
print(teclado[4])
print(teclado[-1])#-1 vai pra ultimo item
print(teclado.index('l'))# index funciona pra localizar a letra da string
print(teclado[teclado.index('l')])

# Acessando partes de uma string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5]) #nunca inlcui o ultimo item solicitado no caso de solicitar ate o 5 ele só ira ate o 4
print(link[0:])  #do inicial ate o final
print(link[-5:]) #começa a contagem de tras pra frente e mostra a quantidade selecionada (nesse caso começa no 1)
print(link[5:])  #começa apartir do numero escolhido 
print(link[:-5]) #se não selecioanr o inicio conta as casas de tras pra frente e retirar elas


frase = 'Clean Code'
print(frase.rindex('C'))

# DESAFIO 1 🥇
# Desafio 1 Encontre o índice de 'o' dentro da variável biblioteca

biblioteca = 'Biblioteca'
print(biblioteca.index('o'))
print(biblioteca[5])
print(biblioteca[biblioteca.index('o')])

# Desafio 2
# Usando a frase
frase = 'Desenvolvimento De Aplicações'
# Imprima apenas 'De Aplicações'
print(frase.rindex('D'))
print(frase[16:])

#resposta do Professor
indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
print(frase[indice_d:indice_s+1])
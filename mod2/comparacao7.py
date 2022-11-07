# Loop for (laços de repetição)
for numero in range(1, 21, 2):  #( range começa do 0 e vai ate o penultimo numero escolhido)(se coloca so o numero inicia do 0, se coloca uma 
    #virgula pode esolher o numero que inicia exempolo 1,6 pra ir do 1 ao 5 ) (se colocar uma segunda virgula ele vai pular os numeros 
    # na quantidade que foi escolhida)
    print('carregando', numero)

nomes = ['jeff', 'carl', 'jean', 'luke']
for nome in nomes:
    print(nome)


# Desafio 1  🥇
# Usando um loop, exiba na tela: Estamos em X
# onde x é um valor iniciando em 18 e finalizando em 110

for numero in range(18, 111):
    print('Estamos em', numero)

# Desafio 2
# Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando loop for a seguinte frase
# "Realizando Passo X"
for numero in range(1, 11):
    print('Realizando passo', numero)
    print(f'Realizando passo {numero}')# exemplo professor
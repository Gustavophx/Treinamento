# continue, ignorar/pular item em um laço
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue

# break, para interromper a interação
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break

frutas = ['Maça', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionar a dieta')

'''# DESAFIOS 🥇

## Desafio 1

Use a operação necessária(break ou continue) para que a seguinte condição aconteça.
* Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela
estilos = ['Hip-Hop','Rock','Rap','Pop']

## Desafio 2 

Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:
* Ao chegar ao estilo "Rock" a execução deve interrompida
estilos = ['Hip-Hop','Rock','Rap','Pop'] '''

estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap': # o '' escolhido não sera adicionado
        continue
    print(estilo)

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)
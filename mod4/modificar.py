'''
Como criar e modificar arquivos
'w'   -> Usado somente para escrever algo
'a'   -> Usado para acrescentar algo
'r'   -> Usado somente para ler algo
'r+'  -> Usado para ler e escrever algo
'''

import os

#with open('celulares.txt', 'w') as arquivo:
#    arquivo.write(' Celular 1')

#numeros = [1, 2, 3, 4, 5, 6]
#with open('numeros.txt', 'a', newline='') as arquivo:
#    for numero in numeros:
#        arquivo.write(str(numero) + os.linesep)



#with open('nomes.txt', 'r')as arquivo:
#    for linha in arquivo:
#        print(linha)

# with open('numeros.txt', 'r+') as arquivo:
#     for linha in arquivo:
#         print(linha)
#     arquivo.write('9000')

# 🥇 DESAFIO Manipulação de Arquivos🥇

'''
Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
# Primeiro crie 3 listas
* Uma lista que contem 5 frutas
* Uma lista que contem 5 cores
* Uma lista que contem 5 linguagens de programação
# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''
import os
'''
frutas = ['Fruta1', 'Fruta2', 'Fruta3', 'Fruta4', 'Fruta5', ]
cores = ['Cor1', 'Cor2', 'Cor3', 'Cor4', 'Cor5']
linguagens = ['Python', 'C#', 'Javascript', 'Java', 'PHP']
# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linguagem ocupe apenas uma linha.
with open('top 5 linuguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)
# BONUS - Como você poderia criar vários arquivos vazios, usando um laço for?
arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass

'''
import os
tests = ['test1', 'test2', 'test3', 'test4']
with open('test.txt', 'w', newline='') as arquivo:
    for test in tests:
        arquivo.write(test + os.linesep)
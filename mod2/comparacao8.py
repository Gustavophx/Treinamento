# Nested Loops (loops aninhados)
# Pais + Estação
paises = ['Brasil', 'india', 'EUA']
estacoes_do_ano = ['primaveira', 'verão', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')


for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno de {y}')

# Desafio
# Imprima na tela a marca + celular de todos celulares, usando as informações abaixo

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')
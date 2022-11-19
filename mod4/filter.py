# Filter
nomes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']

def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False
print(list(filter(pessoa_aprovada, nomes)))

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:   # Pra avaliar algo e preciso escolher o index que sera utilizado entre [] index localizado na lista começa 0,1,2 ...
        return True         # OBS: se não colocar nada no [] irar selecionar a lista toda.
    else:
        return False

print(list(filter(eh_antiguidade, pinturas))) # sempre que usar filter ou Map precisa transforma em lista com o 'LIST'
print(list(map(eh_antiguidade, pinturas))) # Filter mostrar so o que deseja da lista, enquanto o Map mostrar tudo da lista com True ou False
# Usa Filter quando precisa de algo especifico, e Map quando quer analista a lista toda.

# DESAFIO 1 🥇

'''

Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

'''

vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]     

def salario_alto(salario): # o que estiver entre () e paramento pra ser utilizado mais tarde
    if salario[1] >= 2500:
        return True
    else:
        return False

print(list(filter(salario_alto, vagas)))

# Comparação com operadores Booleanos
idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21) and (possui_convite == True)) #(and) adiciona condição
print(idade >= 21 or possui_convite == True) #(or)usado quando uma das condições for aceita serar True

# maior de 21 e possui convite, ou seja filho do dono
print((idade >= 21 and possui_convite == True) or (filho_do_dono == True)) #separar as opções entre parentes pra deixar mais organizado

# Exemplo
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
# Você só pode trabalhar aqui se for maior de idade e possuir carteira de trabalho
print((maior_de_idade == True) and (possui_carteira_de_trabalho == True))
print(maior_de_idade and possui_carteira_de_trabalho) #simplificando o codigo,
# Queremos contratar pessoas que ainda não possuem um veículo próprio, mas já possuam uma carteira de trabalho
print((possui_carteira_de_trabalho == True) and not possui_veiculo_proprio)


# Desafio 🥇

'''
Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False
E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.
Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for menor de idade
Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
'''
possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print((possui_passaporte == True and passagem_comprada == True) and not menor_de_idade) # Da pra simplificar tirando os True pois são desncessecarios

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((possui_passaporte == True or passagem_comprada == True) and not menor_de_idade)

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte or passagem_comprada == True) and not menor_de_idade)

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print((not possui_passaporte or not passagem_comprada) and menor_de_idade) #quando ouver ou na frase e "or not"
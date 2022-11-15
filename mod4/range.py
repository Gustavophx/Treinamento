# Range(Geradores)
print(type(range(30)))
for numero in range (30): # primeiro valor sempre sera 0 se não especificado, ate o penultimo valor do informado.
    print(numero)
for numero in range(10,30):# 'valor inicial definido'
    print(numero)
# Quando quiser a opção de dar pulos entre os valores na 3 index do range() digite o valor EX: x,x,2
for numero in range (10,30,2):
    print(numero)

# Criar listas mais rapidamente
resultado = list(range(0,201,10))
print(resultado)
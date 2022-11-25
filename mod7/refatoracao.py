# Refatoração
class Calculadora:  # Caso precise alterar o nome dado, aperte F2 e enter, caso queira ver antes o que sera mudado F2 e depois shift+ enter
    pass


calc1 = Calculadora()
cals2 = Calculadora()
calc3 = Calculadora()

print(calc1)

# Utilizar comando CTRL+Shift+R pra criar uma função automaticamente  "Extract Method"
def calc():
    resultado = 20 + 50

calc()

# Urilizar comando CTRL+Shift+R pra extrair variavel e criar uma variavel "Extract Variable"
altura = 60
largura = 2
tamanho = (altura/largura) + 50

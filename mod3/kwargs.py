# ** Kwargs(Keyword arguments) - Funções com nº de argumentos nomeados
def concatenar(**palavras): # ** duplo, argumentos nomeados em quantidade infinita
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')

# * = argumento posicionais, ** argumentos nomeados (sempre serar seguido de 'ex'='argumento')


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('jeff', 1,2,3,4,a=5,b=6,c=7)
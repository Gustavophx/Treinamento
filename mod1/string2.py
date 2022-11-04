nome_curso = ' Edição de Vídeo '
print(nome_curso.upper())#Maiuscula
print(nome_curso.lower())#minuscula
print(nome_curso.strip())#retirar todo espaço entre "" ou ''
print(nome_curso.lstrip())#retirar espaço a < (l)eft (esquerda)
print(nome_curso.rstrip())#retirar espaço a > (right)(direita)
print(nome_curso.find('ção'))# Função de localização depois do ' ou "
print(nome_curso.replace('Vídeo', 'Música'))#troca a palavra selecionada pela a proxima.
print('https://sc.olx.com.br/?o=90&q=relogio' .replace('relogio', 'carro'))


# Desafio
# Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
print('É melhor FEITO que PERFEITO')


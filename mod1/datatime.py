from datetime import datetime 

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data

lancamento_app = datetime(2021,5,28)
print(lancamento_app)

# Quero receber a data lançamento do meu aplicativo
# formato de data brasileiro dia/mes/ano
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
print(type(data_de_lancamento))

# Calcular o prazo entre datas
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

# DESAFIO 🥇

# Calcule quantos dias faltam até o seu aniversário
from datetime import datetime
aniversario = datetime.strptime(input('Data de aniversario ? '), '%d/%m/%Y')
data_atual = datetime.now()
proximo_aniversario = aniversario - data_atual
print(proximo_aniversario.days)

# Resposta professor

from datetime import datetime
aniversario2 = datetime (2023, 2, 28)
dias_para_aniversario = aniversario2 - datetime.now()
print(dias_para_aniversario)
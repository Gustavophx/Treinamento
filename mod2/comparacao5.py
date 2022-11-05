# If elif else
trabalho_terminado = False
if trabalho_terminado == True: #primeiro compara com o resultado esperado do if depois irar pra else
    print('Bora dar uma saida!')
else:
    print('Não posso sair agora.')
# if condicao
    # comandos a serem executados Ex. print msg com confirmação ou negação

numero_atrasos = 2
if numero_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa e sua primeira falta')
else:
    print('Pode entrar')

'''
A velocidade máxima para essa rua é 50km
* Cruzou entre 50km a 60km , levou multa de 2 pontos
* Cruzou entre 61km a 75km , levou multa de 3 pontos
* Cruzou acima de 75km , levou multa de 7 pontos
'''
velocidade = 55
if velocidade <= 50:
    print('Não foi multado')
#elif velocidade >= 51 and velocidade <= 60: outra forma de fazer
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('levou multa de 7 pontos')


# Desafio 🥇

# Monte o seguinte cenário usando condicionais
# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras
# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices
'''
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
Acima de 50cm Favor consultar na recepção
# Declare uma variável que represente o tamanho atual do cabelo
# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário '''

tamanho = 51
if tamanho <= 20:
    print('Valor R$ 50,00')
elif tamanho >= 21 and tamanho <= 30:
    print('Valor R$ 70,00')
elif tamanho >= 31 and tamanho <= 50:
    print('Valor R$ 100,00')
else:
    print('Favor consultar na recepção! ')

# Versão chaining (ou resumida)
if tamanho <= 20:
    print('Pagar R$ 50,00')
elif 21 <= tamanho <= 31:
    print('Pagar R$ 70,00')
elif 31 <= tamanho <= 50:
    print('Pagar R$ 100,00')
else:
    print('Favor consultar na recepção! ')
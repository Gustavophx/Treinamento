import webbrowser
import threading
import time
import random


""" def extrair_dados_do_site(site):
    print(f'Eestamos navegando até o site {site}')
    webbrowser.open_new(site)
    for i in range(1, 21):
        print(f'Processando dados - {i}/20')
        time.sleep(1)
    print('Finalizado extração de dados do site')


def baixar_arquivos():
    for i in range(1, 10):
        print(f'Baixando arquivos - {i}/10')
        time.sleep(1)
    print('Arquivos baixados')


nova_thread = threading.Thread(target=extrair_dados_do_site, args=(
    'https:www.google.com',), daemon=True)  # no args lembra de finalizar com , mesmo com 2 args site/algo mais
nova_thread.start()
baixar_arquivos()
nova_thread.join()  """
# usar o .start e outra função depois o .join caso queira execução conjunta, caso precise esperar o resultado de algo primeiro
# utilize .start .join e depois a função, caso precise esperar e thread finalizar e coleta a informação.

""" def comentar(site,comentario):
    print(f'Entrando no site: {site}')
    print(f'Deixando um comentário {comentario}')
    time.sleep(5)
    print(f'Dados processados no site: {site}')

comentarios = ['oi', 'olá', 'gostei', 'curti', 'muito bom']
threads = []
for site in range(6):
    nova_thread = threading.Thread(target=comentar, args=(site,random.choice(comentarios)))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finalizando {thread.name}') """


# Desafio 1

""" def baixando_fotos(site):
    print(f'Baixando fotos no site {site}')

def acessando_site(site):
    print(f'Estamos acessando o site {site}')


nova_thread = threading.Thread(target=baixando_fotos, args=('https://www.facebook.com',),daemon=True)
nova_thread.start()
acessando_site('htps://www.facebook.com')
nova_thread.join() """


# Desafio 2 

def extrair_preco(site, produto):
    print(f'Navegando até o site {site} e pesquisando sobre {produto}')
    time.sleep(5)
    print(f'{produto} processado com sucesso')

produto = ['celular', 'monitor', 'fone de ouvido', 'alto-falante', 'computador']
threads = []

for i in range(5):
    nova_thread = threading.Thread(target=extrair_preco, args=('https://www.mercadolivra.com', produto[i]))
    threads.append(nova_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


# Classes e Intro a POO
# Código solto
""" marca = input('Digitar a marcar do seu computador: ')
memoria = input('Digitar a quantidade de memória ram: ')
placa = input('Digite o nome da placa de vídeo: ')

print(f'Seu computador é da marca: {marca}')
print(f'Seu computador possui {memoria} de memória')
print(f'Seu computador possui uma placa de vídeo: {placa}')
 """

# Mover comandos repetitivos
# Funções
""" def exibir_informacoes_do_computador():
    marca = input('Digitar a marcar do seu computador: ')
    memoria = input('Digitar a quantidade de memória ram: ')
    placa = input('Digite o nome da placa de vídeo: ')

    print(f'Seu computador é da marca: {marca}')
    print(f'Seu computador possui {memoria} de memória')
    print(f'Seu computador possui uma placa de vídeo: {placa}')

exibir_informacoes_do_computador() """

# Classes

class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

# Marca, Memória ram, Placa de vídeo
computador1 = Computador('Asus', '8Gb', 'Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video) 
computador2 = Computador('Dell', '4Gb', 'ATI')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video) 
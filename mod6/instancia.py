# Métodos comuns

class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)

# Métodos de Classe (CLass Methods)

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Baixo Custo')

    @classmethod
    def computador_cofiguracao_pesada(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - ALto Nível')

    @staticmethod # Métodos estáticos (Static Methods)
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

print(Computador.roda_programas_pesados(10))


# Configuração p/ cliente de escritório
computador1 = Computador.computador_escritorio('8GB')

# Configuração para cliente de trabalho pesado(jogos,vídeo,3D)
computador2 = Computador.computador_cofiguracao_pesada('32GB')

computador1.exibir_dados_do_computador()
print('#####')
computador2.exibir_dados_do_computador()

# Métodos estáticos (Static Methods)

@classmethod
def computador_cofiguracao_pesada(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - ALto Nível')

@staticmethod
def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

print(Computador.roda_programas_pesados(10))
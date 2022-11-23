# Classes abstratas 
# Criar um contrato(esqueleto) -> que deve ser implementado na class que a herda
from abc import ABC,abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self,tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando a lente para {tamanho}')

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)


# Desafio

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self,brilho):
        pass
    @abstractmethod
    def diminuir_claridade(self,brilho):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, brilho):
        print(f'Aumentando a claridade em {brilho} pontos')
    def diminuir_claridade(self, brilho):
        print(f'Diminuindo a claridade em {brilho} pontos')


monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.diminuir_claridade(5)

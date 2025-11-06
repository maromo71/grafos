# fila_atendimento.py
# Contem a classe que gerencia a Fila de Prioridade
import heapq
import itertools
from prioridade import Prioridade

class FilaAtendimento:
    """
    Representa uma fila de atendimento de pacientes
    usando uma fila de prioridade, registrando tambem
    a ordem de chegada Min-Heap
    """
    def __init__(self):
        self._fila = []
        self._contador = itertools.count()

    def adicionar_paciente(self, nome, prioridade):
        """Adiciona um paciente a fila de atendimento."""
        if not isinstance(prioridade, Prioridade):
            raise ValueError("Prioridade invalida")
        contagem_chegada = next(self._contador)
        entrada = (prioridade.value, contagem_chegada, nome)
        heapq.heappush(self._fila, entrada)
        print(f"Paciente {nome} Prioridade {prioridade.name} foi adicionado")
        print(f"Posicao na fila geral de atendimento: {len(self._fila)}")

    def chamar_proximo_paciente(self):
        """Chama o proximo paciente na fila, de maior prioridade"""
        if len(self._fila) == 0:
            print("Nenhum paciente na fila")
            return None
        
        prioridade_num, _, nome = heapq.heappop(self._fila)
        prioridade_nome = Prioridade(prioridade_num).name
        print(f"\n[! Pronto] - Proximo paciente a ser atendido")
        print(f"| Nome: {nome:20} | Prioridade: {prioridade_nome:12} |")

    def __len__(self):
        """Retornar o numero de pacientes na fila"""
        return len(self._fila)
    

# prioridade.py
# definindo os modulos necessarios: Enum e 
# IntEnum para definir as prioridades

from enum import IntEnum

class Prioridade(IntEnum):
    EMERGENCIA = 1
    URGENCIA = 2
    PREFERENCIAL = 3
    NORMAL = 4

def __str__(self):
    return self.name
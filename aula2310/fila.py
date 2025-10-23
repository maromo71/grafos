# fila.py - Usando deque para implementar uma fila
from collections import deque

def criar_fila():
    """
        Cria e retorna um fila nova usando deque.
    """
    return deque()

def adicionar_elemento(fila, elemento):
    """
        Adiciona um elemento ao final da fila.
        Arguments:
            fila -- A fila onde o elemento será adicionado.
            elemento -- O elemento a ser adicionado à fila.
    """
    fila.append(elemento)

def remover_elemento(fila):
    """
        Remove e retorna o elemento do início da fila.
        Arguments:
            fila -- A fila de onde o elemento será removido.
        Returns:
            O elemento removido da fila.
            ou None se a fila estiver vazia.
    """
    if fila:
        return fila.popleft()
    else:
        None

def mostrar_fila(fila):
    """
        Mostra os elementos atuais na fila.
        Arguments:
            fila -- A fila cujos elementos serão mostrados.
        Returns:
            Uma lista dos elementos na fila.
    """
    if fila:
        return list(fila)
    else:
        return None
    
def mostrar_proximo(fila):
    """
        Mostra o próximo elemento na fila sem removê-lo
        Arguments:
            fila -- A fila cujo próximo elemento será mostrado.
        Returns:
            O próximo elemento na fila.
            ou None se a fila estiver vazia.
    """
    if fila:
        return fila[0]
    else:
        return None
    
def mostrar_ultimo(fila):
    """
        Mostra o último elemento na fila sem removê-lo
        Arguments:
            fila -- A fila cujo último elemento será mostrado.
        Returns:
            O último elemento na fila.
            ou None se a fila estiver vazia.
    """
    if fila:
        return fila[-1]
    else:
        return None
    
def tamanho_fila(fila):
    """
        Retorna o tamanho atual da fila.
        Arguments:
            fila -- A fila cujo tamanho será retornado.
        Returns:
            O número de elementos na fila.
    """
    return len(fila)

def fila_vazia(fila):
    """
        Verifica se a fila está vazia.
        Arguments:
            fila -- A fila a ser verificada.
        Returns:
            True se a fila estiver vazia, False caso contrário.
    """
    return len(fila) == 0
# arquivo bfs.py - Algoritmo de Busca em Largura (BFS)

from collections import deque

def bfs(grafo):
    caminho = set()
    visitados = set()
    componentes = 0

    for vertice in grafo:
        if vertice not in visitados:
            componentes += 1
            print(f"Vertice Inicio: {vertice}")
            print(f"Componente Conectado: {componentes}")
            #BFS para este componente
            fila = deque([vertice])
            visitados.add(vertice)

            while fila:
                vertice_atual = fila.popleft()
                print(f"Processa: {vertice_atual}")
                caminho.add(vertice_atual)
                for vizinho in grafo[vertice_atual]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)
                print(f"Fila {vertice_atual}: {list(fila)}")
            print(f"Caminho ate agora: {caminho}\n")

            print(f"Componente {componentes} completo.\n")
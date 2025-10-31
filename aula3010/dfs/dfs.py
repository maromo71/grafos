def dfs(grafo):
    visitados = set()
    componentes = []
    for vertice in grafo:
        if vertice not in visitados:
            pilha = [vertice]
            visitados.add(vertice)
            componente_atual = []
            while pilha:
                atual = pilha.pop()
                componente_atual.append(atual)
                for vizinho in grafo[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
                        visitados.add(vizinho)
            componentes.append(componente_atual)
    return componentes



def montar_grafo():
    # definir um grafo nao dirigido com base no 
    # exemplo do slide 29 material 05
    G = {
        'v1': ['v2', 'v3', 'v4'],
        'v2': ['v1', 'v3'],
        'v3': ['v1', 'v2'],
        'v4': ['v1']
    }
    return G

def calcular_grau_do_vertice(G):
    # para ver o grau de CADA vertice
    soma = 0
    for v in G:
        print(f"Grau de {v}: {len(G[v])}")
        soma += len(G[v])
    
    return soma / 2


def lista_adjascencia(G):
    # para ver os vizinhos de CADA vertice
    for v in G:
        print(f"Vizinhos de {v}: {G[v]}")

 

def main():
    # chamar o metodo para montar o grafo
    G = montar_grafo()
    # chamar o metodo para exivir a lista
    lista_adjascencia(G)
    # chamar o método para exibir o numero de graus de cada vertice
    arestas = calcular_grau_do_vertice(G)

    print(f"Numero de arestas deste grafo: {arestas}")

if __name__ == "__main__":
    main()
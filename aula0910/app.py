from grafo import Grafo

def main():
    meu_grafo = Grafo()

    print("Criando Grafo da Figura na Lousa")

    #1. Adicionar os os quatro vertices
    vertices = ["V1", "V2", "V3", "V4"]

    #2. Varrer a lista acima e invocar o metodo acionar vertice
    for vertice in vertices:
        meu_grafo.adicionar_vertice(vertice)

    print("\n")
    #3. Adicionar as arestas, especificando seus nome e os vertices
    # que elas conectam
    meu_grafo.adicionar_aresta("E1", "V1", "V2")
    meu_grafo.adicionar_aresta("E2", "V1", "V3")
    meu_grafo.adicionar_aresta("E3", "V1", "V4")
    meu_grafo.adicionar_aresta("E4", "V2", "V3")

    #4. Por fim exibir a lista de incidencia
    meu_grafo.mostrar_lista_incidencia()

if __name__ == "__main__":
    main()
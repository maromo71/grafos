from grafo import Grafo

def main():
    meu_grafo = Grafo()

    print("Criando Grafo da Figura na Lousa")

    #1. Adicionar os os quatro vertices
    vertices = ["Luz", "Sé", "Paraiso", "Consolacao", "Republica"]

    #2. Varrer a lista acima e invocar o metodo acionar vertice
    for vertice in vertices:
        meu_grafo.adicionar_vertice(vertice)

    print("\n")
    #3. Adicionar as arestas, especificando seus nome e os vertices
    # que elas conectam
    meu_grafo.adicionar_aresta("Linha Azul", "Sé", "Luz")
    meu_grafo.adicionar_aresta("Linha Vermelha", "Sé", "Republica")
    meu_grafo.adicionar_aresta("Linha Verde", "Paraiso", "Consolacao")
    meu_grafo.adicionar_aresta("Conexao Se Paraiso", "Sé", "Paraiso")
    meu_grafo.adicionar_aresta("Conexa Luz Consolacao", "Luz", "Consolacao")

    #4. Por fim exibir a lista de incidencia
    meu_grafo.mostrar_lista_incidencia()

if __name__ == "__main__":
    main()
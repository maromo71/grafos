class Grafo:
    def __init__(self):
        #dicionario que armazenara a lista de incidencia
        self.vertices = {}
        #dicionario para armazenar as informacoes de cada aresta
        self.arestas = {}

    def adicionar_vertice(self, nome_vertice):
        if nome_vertice not in self.vertices:
            self.vertices[nome_vertice] = []
            print(f"Vertice {nome_vertice} adicionado com sucesso!")
        else:
            print(f"Vertice {nome_vertice} ja existe!")

    def adicionar_aresta(self, nome_aresta, vertice1, vertice2):
        #Adicionar uma aresta conectar a dois vertices
        if vertice1 not in self.vertices or vertice2 not in self.vertices:
            print(f"Erro: Vertice {vertice1} ou {vertice2} nao existe!")
            return
        #Adicionar a aresta no dicionario de arestas
        self.arestas[nome_aresta] = (vertice1, vertice2)

        self.vertices[vertice1].append(nome_aresta)
        self.vertices[vertice2].append(nome_aresta)
        print(f"Aresta {nome_aresta} adicionada com sucesso!")


    def mostrar_lista_incidencia(self):
        print("Lista de Incidencia:")
        if not self.vertices:
            print("O grafo esta vazio!")
            return
        
        for vertice, arestas_incidentes in self.vertices.items():
            print(f"Vertice {vertice}: {arestas_incidentes}")
            

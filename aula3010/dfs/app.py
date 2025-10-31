from dfs import dfs
def main():
    grafo = {
        0: [9, 1],
        1: [8, 0],
        2: [3],
        3: [7, 5, 4, 2],
        4: [3],
        5: [6, 3],
        6: [7, 5],
        7: [11, 10, 8, 6, 3],
        8: [9, 7, 1],
        9: [9, 0],
        10: [11, 10],
        11: [10, 7],
        12: [] # Vértice isolado
    }
    print("Grafo analisado")
    for vertice, vizinhos in grafo.items():
        print(f"{vertice}: {vizinhos}")
    
    print("\n" + "*" * 60 + "\n")
    # executa a funcao dfs passando o grafo acima
    # desta forma obtermos os componentes
    componentes = dfs(grafo)
    print(f"Numero de componentes encontrados: {len(componentes)}")
    print("\n" + "*" * 60 + "\n")

    for i, componente in enumerate(componentes, 1):
        print(f"Componente {i}: {componente}")
    print("\n" + "*" * 60 + "\n")


if __name__ == "__main__":
    main()
def montar_grafo():
    # definir um grafo nao dirigido com base no 
    # exemplo do slide 29 material 05
    G = {
        'MMI': ['ITA', 'MGU'],
        'MGU': ['PIN', 'EST', 'MMI', 'ITA'],
        'EST': ['MGU'],
        'ITA': ['MGU', 'MMI','JCU'],
        'PIN': ['MGU', 'JCU'],
        'JCU': ['PIN', 'ITA']
    }
    return G

def calcular_grau_do_vertice(G):
    # para ver o grau de CADA vertice
    soma = 0
    contar_impar = 0
    for v in G:
        print(f"Grau de {v}: {len(G[v])}")
        soma += len(G[v])
        if len(G[v]) % 2 != 0:
            contar_impar += 1
    
    print(f"Numero de vertices com grau impar: {contar_impar}")
    if contar_impar == 0:
        print("Todos os vertices tem grau par. Existe um circuito euleriano")
        print("um caminho que comeca e termina no mesmo ponto")
    elif contar_impar == 2:
        print("Existe exatamente dois graus impar. Existe um caminho euleriano")
        print("que passa por todos os vertices apenas uma vez. comeca no")
        print("que tem grau impar para terminar no mesmo ponto")
    else:
        print("Nao formam um caminho euleriano")


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
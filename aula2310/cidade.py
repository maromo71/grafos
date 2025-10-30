from collections import deque

def bfs(grafo, no_inicial, no_final):
  """
  Realiza uma Busca em Largura (BFS) em um grafo para encontrar o caminho mais curto
  entre um no_inicial e um no_final.

  Args:
    grafo: Um dicionário representando o grafo onde as chaves são nós
           e os valores são listas de seus vizinhos.
    no_inicial: O nó de partida para a busca.
    no_final: O nó de destino para a busca.

  Returns:
    Uma lista representando o caminho mais curto do no_inicial ao no_final,
    ou None se nenhum caminho for encontrado.
  """
  visitados = set()
  fila = deque([(no_inicial, [no_inicial])])  # Armazena o nó e o caminho para alcançá-lo

  while fila:
    (no_atual, caminho) = fila.popleft()

    if no_atual == no_final:
      return caminho

    if no_atual not in visitados:
      visitados.add(no_atual)
      for vizinho in grafo.get(no_atual, []): # Usa .get() para lidar com nós potencialmente ausentes
        if vizinho not in visitados:
          fila.append((vizinho, caminho + [vizinho]))

  return None # Nenhum caminho encontrado

def main():
  print("\nCaminho mais curto no grafo de cidades:")
  grafo_cidades = {
    "Mogi Mirim": ["Mogi Guaçu", "Itapira"],
    "Mogi Guaçu": ["Mogi Mirim", "Itapira", "Espírito Santo do Pinhal", "Estiva Gerbi"],
    "Itapira": ["Mogi Mirim", "Mogi Guaçu", "Jacutinga"],
    "Jacutinga": ["Itapira", "Espírito Santo do Pinhal"],
    "Espírito Santo do Pinhal": ["Mogi Guaçu", "Jacutinga"],
    "Estiva Gerbi": ["Mogi Guaçu"],
    "Santos": ["Guarujá"],
    "Guarujá": ["Santos", "São Paulo"],
    "São Paulo": ["Guarujá"]
  }
  cidade_inicio = "Jacutinga"
  cidade_fim = "Guarujá"
  caminho_mais_curto_cidades = bfs(grafo_cidades, cidade_inicio, cidade_fim)
  if caminho_mais_curto_cidades:
    print(f"Caminho mais curto de {cidade_inicio} para {cidade_fim}: {caminho_mais_curto_cidades}")
  else:
    print(f"Nenhum caminho encontrado de {cidade_inicio} para {cidade_fim}")


if __name__ == "__main__":
  main()
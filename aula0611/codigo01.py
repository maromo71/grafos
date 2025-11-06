# codigo01.py
# criar uma fila de prioridade com o heapq
import heapq
import time
# 1. definir a fila de prioridade
fila = []

# 2. inserir elementos na fila de prioridade
heapq.heappush(fila, 37)
heapq.heappush(fila, 13)
heapq.heappush(fila, 7)
heapq.heappush(fila, 29)
heapq.heappush(fila, 16)
heapq.heappush(fila, 42)

print("Fila: ",fila)

# 3. remover o menor elemento enquanto houver elementos
while fila:
    menor = heapq.heappop(fila)
    print("Menor elemento removido:", menor)
    print("Fila atualizada:", fila)
    time.sleep(1)
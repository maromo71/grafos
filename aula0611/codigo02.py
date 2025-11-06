# codigo02.py
# lista de tarefas diarias com prioridade
import heapq
import time
# 1. definir a fila de prioridade
# Prioridade [1 é mais alta, 5 é mais baixa]
tarefas = []

# 2. inserir tarefas na fila com prioridade
heapq.heappush(tarefas, (2, "Estudar Python"))
heapq.heappush(tarefas, (1, "Materiais Estudar"))
heapq.heappush(tarefas, (3, "Trabalho de escola"))
heapq.heappush(tarefas, (3, "Trabalho de casa"))
heapq.heappush(tarefas, (5, "Dormir"))
heapq.heappush(tarefas, (4, "Ler o livro da Maria"))

# 3. espiar o menor elemento sem removê-lo
print("Tarefa mais urgente:", tarefas[0])

# 4. remover a tarefa mais urgente enquanto houver tarefas
# criando uma nova lista para verificar a ordem em que foram
# feitas
tarefas_feitas = []
while tarefas:
    prioridade, tarefa = heapq.heappop(tarefas)
    tarefas_feitas.append(tarefa)
    print("Tarefa feita:", tarefa)
    time.sleep(1)

print("Registro das tarefas feitas abaixo: ")
for tarefa in tarefas_feitas:
    print(tarefa)

# ultima tarefa feita no dia
print("Ultima tarefa feita:", tarefas_feitas[-1])
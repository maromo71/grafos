class Stack:
    def __init__(self):
        """Criando uma pilha"""
        self.items = []

    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return len(self.items) == 0
    
    def push(self, item):
        """Adiciona um item na pilha"""
        self.items.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha"""
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        """Retorna o item do topo da pilha sem removê-lo"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        """Retorna o número de itens na pilha"""
        return len(self.items)
    
    def show_stack(self):
        """Mostra a pilha na ordem top-botton"""
        print(f"Elementos da pilha")
        print(f"*"*30)
        total = len(self.items)
        for i in range(total-1, -1, -1):
            print(f"| {i} - {self.items[i]}")
        print(f"*"*30)
    

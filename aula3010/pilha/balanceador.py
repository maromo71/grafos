from stack import Stack
import os

def validar_expressao(expressao):
    """
    supondo que a expressao seja: (5 + 3) * [2 * {3-1}]
    Verificar se a expressao esta
    balanceada com (, [, { e }, ], )
    """
    pilha = Stack()
    for caractere in expressao:
        if caractere in ["(", "[", "{"]:
            pilha.push(caractere)
        elif caractere in [")", "]", "}"]:
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (topo == "(" and caractere != ")") or \
               (topo == "[" and caractere != "]") or \
               (topo == "{" and caractere != "}"):
                return False
            
    return pilha.is_empty()


expressao = "(5 + 3) * [2 * {3-1}]"
if validar_expressao(expressao):
    print("Expressao valida")
else:
    print("Expressao invalida")
            
     
        
    

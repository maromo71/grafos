from stack import Stack
import os

def menu():
    """Exibe o menu de opcoes"""
    os.system('cls')
    print("Escolha uma opcao")
    print("1 - Empilhar")
    print("2 - Desempilhar")
    print("3 - Espiar Topo")
    print("4 - Mostrar Pilha")
    print("5 - Tamanho da Pilha")
    print("6 - Esta vazia ?")
    print("7 - Sair")

def main():
    """Funcao principal - fluxo do programa"""
    pilha = Stack()
    while True:
        menu()
        opcao = int(input("Opcao: "))
        if opcao == 1:
            item = input("Digite o item a ser empilhado")
            pilha.push(item)
            print(f"{item} empilhado com sucesso")
            input("Pressione ENTER para continuar")
        elif opcao == 2:
            item = pilha.pop()
            if item is not None:
                print(f"Item desempilhado: {item}")
            else:
                print("Pilha vazia")
            input("Pressione ENTER para continuar")
        elif opcao == 3:
            item = pilha.peek()
            if item is not None:
                print(f"Item no topo: {item}")
            else:
                print("Pilha vazia")
            input("Pressione ENTER para continuar")
        elif opcao == 4:
            pilha.show_stack()
            input("Pressione ENTER para continuar")
        elif opcao == 5:
            tamanho = pilha.size()
            print(f"Tamanho da pilha: {tamanho}")
            input("Pressione ENTER para continuar")
        elif opcao == 6:
            esta_vazia = pilha.is_empty()
            if esta_vazia:
                print("A pilha está vazia")
            else:
                print("A pilha não está vazia")
            input("Pressione ENTER para continuar")
        elif opcao == 7:
            print("Saindo do programa")
            break
        else:
            print("Opcao invalida")
            input("Pressione ENTER para continuar")
            
if __name__ == "__main__":
    main()
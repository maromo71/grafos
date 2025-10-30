from stack import Stack
import os

def menu():
    """Exibe o menu de opcoes"""
    os.system('cls')
    print("Escolha uma opcao")
    print("1. Entrada da Frase ")
    print("2. Saida da Frase ")
    print("3. Sair")

def main():
    """Funcao principal - fluxo do programa"""
    pilha = Stack()
    while True:
        menu()
        opcao = int(input("Opcao: "))
        if opcao == 1:
            frase = input("Digite a frase: ")
            for palavra in frase.split():
                pilha.push(palavra)
            input("Pressione ENTER para continuar")
        elif opcao == 2:
            frase_invertida = ""
            while not pilha.is_empty():
                frase_invertida += pilha.pop() + " "
            print(f"Frase invertida: {frase_invertida}")
            input("Pressione ENTER para continuar")
        elif opcao == 3:
            print("Saindo do programa")
            break
        else:
            print("Opcao invalida")
            input("Pressione ENTER para continuar")

if __name__ == "__main__":
    main()
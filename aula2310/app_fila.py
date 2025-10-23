from fila import *
import os

def menu():
    os.system("cls") # use cls para limpar a tela no Windows
    print("="*60)
    print("| Hospital Fila de Espera |")
    print("="*60)
    print("1. Adicionar paciente à fila")
    print("2. Chamar proximo paciente")
    print("3. Mostrar proximo paciente  da fila")
    print("4. Mostrar ultimo paciente da fila")
    print("5. Mostrar todos os pacientes na fila")
    print("6. Verificar tamanho da fila")
    print("7. Verificar se a fila está vazia")
    print("8. Sair")
    print("="*60)

def main():
    fila = criar_fila()
    while True:
        menu()
        escolha = int(input("Escolha uma opção (1-8): "))
        
        if escolha == 1:
            paciente = input("Digite o nome do paciente: ")
            adicionar_elemento(fila, paciente)
            print(f"Paciente {paciente} adicionado à fila.")
            os.system("pause") # aguarda uma tecla para continuar
        elif escolha == 2:
            paciente = remover_elemento(fila)
            if paciente:
                print(f"Próximo paciente chamado: {paciente}")
            else:
                print("Nao há mais pacientes em espera.")
            os.system("pause")
        elif escolha == 3:
            paciente = mostrar_proximo(fila)
            if paciente:
                print(f"Próximo paciente na fila: {paciente}")
            else:
                print("Não há pacientes na fila.")
            os.system("pause")
        elif escolha == 4:
            paciente = mostrar_ultimo(fila)
            if paciente:
                print(f"Último paciente na fila: {paciente}")
            else:
                print("Não há pacientes na fila.")
            os.system("pause")
        elif escolha == 5:
            pacientes = mostrar_fila(fila)
            if pacientes:
                print(f"Pacientes na fila: {list(pacientes)}")
            else:
                print("Não há pacientes na fila.")
            os.system("pause")
        elif escolha == 6:
            tamanho = tamanho_fila(fila)
            print(f"Tamanho da fila: {tamanho}")
            os.system("pause")
        elif escolha == 7:
            if fila_vazia(fila):
                print("A fila está vazia.")
            else:
                print("A fila não está vazia.")
            os.system("pause")
        elif escolha == 8:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            os.system("pause")

if __name__ == "__main__":
    main()
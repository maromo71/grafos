def avaliar_media(nota):
    if nota < 5:
        return "Reprovado"
    elif nota < 7:
        return "Recuperação"
    else:
        return "Aprovado"

def main():
    for i in range(3):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        resultado = avaliar_media(nota)
        print(f"{nome} - {resultado}")

if __name__ == "__main__":
    main()
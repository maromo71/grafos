def avaliar_nota(nota):
    if 0 <= nota <=10:
        if nota >= 7:
            return "Aprovado"
        elif nota >=5:
            return "Recuperação"
        else:
            return "Reprovado"
    else:
        return "Nota inválida"
    
# exemplo de teste
for i in range(3):
    nota = float(input("Digite a nota do aluno: "))
    print(f"Situacao = {avaliar_nota(nota)}")
alunos = {
    "Antonio": [7.3, 8.7, 9.0],
    "Maria": [7.1, 8.3, 9.0],
    "Ana": [8.3, 7.1, 8.0],
    "Oscar": [0.0, 5.3, 8.0]
}
# calculando a media de cada aluno
# exibindo os aprovados com media >= 7
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media >=7:
        print(f"{nome}: {media:.2f}")
    else:
        print(f"{nome} - REPROVADO")


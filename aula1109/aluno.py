# arquivo aluno.py - Representa nossa classe Aluno
class Aluno:
    # atributo da classe
    numero_alunos = 0

    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        Aluno.numero_alunos += 1

    def matricular(self):
        print(f"Aluno {self.nome} matriculado com sucesso")
        print(f"Passar na sec. e pegar o num de matricula: {self.matricula}")

    def cancelarMatricula(self):
        print(f"Aluno {self.nome} cancelou a matricula")
        print(f"Favor pagar o ultimo mes.")

    def apresentarDados(self):
        print(f"Dados do Aluno de Matr: {self.matricula} ")
        print("*"*50)
        print(f"Nome:  {self.nome} ")
        print(f"Curso: {self.curso} ")
        print("*"*50)


# Simular dois alunos. o Primeiro vou matricular e em seguida cancelar a matricula
# O Segundo vou apenas matricular e apresentar os dados do mesmo.

aluno1 = Aluno(123, "Antonio Carlos da Silva", "EC")
aluno2 = Aluno(234, "Maria da Silva", "EC")

print(type(aluno1)) # -> saida <class '__main__.Aluno'>
print(type(aluno2)) # -> saida <class '__main__.Aluno'>

aluno1.matricular()
aluno1.cancelarMatricula()

aluno2.matricular()
aluno2.apresentarDados()
aluno3 = Aluno(457, "Chico", "EC")

print(Aluno.numero_alunos) # -> saida 2
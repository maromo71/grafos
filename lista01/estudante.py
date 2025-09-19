class Estudante:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida.")

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0
        
    def exibir_perfil(self):
        media = self.calcular_media()
        print("====== Perfil do Aluno ========")
        print(f"Matrícula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Notas: {self.notas}")
        print(f"Média: {media:.2f}")
        print("===============================")


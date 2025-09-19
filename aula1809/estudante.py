class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida. A nota deve estar entre 0 e 10.")
    def calcular_media(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0
    
    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        if self.notas:
            print(f"Notas: {self.notas}")
            print(f"Média: {self.calcular_media()}")
        else:
            print("Este estudante não possui notas.")
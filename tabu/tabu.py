import random

class Tabuleiro:
    def __init__(self):
        # Inicializa uma matriz 10x10 com valores aleatórios entre 1 e 100
        self.matriz = []
        self.palpite1 = 0
        self.palpite2 = 0

        for _ in range(10):
            linha = []
            for _ in range(10):
                valor = random.randint(1, 100)
                # adicionando o valor na linha
                linha.append(valor)
            # adicionando a linha na matriz
            self.matriz.append(linha)
    

    def jogar(self, p1, p2):
        self.palpite1 = p1
        self.palpite2 = p2
        cont = 0
        for linha in self.matriz:
            for valor in linha:
                if valor == self.palpite1 or valor == self.palpite2:
                    cont += 1
        self.exibir_tabuleiro()
        if cont >= 3:
            return cont * 1000.0
        else:
            return 0.0
    
    def exibir_tabuleiro(self):
        for linha in self.matriz:
            for valor in linha:
                if valor == self.palpite1 or valor == self.palpite2:
                    print(f"[{valor:3d}] *", end=" ")
                else:
                    print(f"[{valor:3d}]  ", end=" ")
            print()




#demonstrando
p1 = int(input("digite o palpite 1: "))
p2 = int(input("digite o palpite 2:"))
tabuleiro = Tabuleiro()
resultado = tabuleiro.jogar(p1, p2)
if resultado > 0.0:
    print(f"Parabéns seu premio {resultado:.2f}")
else:
    print("que pena, voce perdeu")

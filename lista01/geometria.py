class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * (self.raio * self.raio)
    
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio
from geometria import Circulo

# Demonstracao
raio = float(input("Digite o raio do circulo: "))
circulo = Circulo(raio)
area = circulo.calcular_area()
circunferencia = circulo.calcular_circunferencia()
print(f"Area do circulo: {area}")
# formatar em duas casas decimais
print(f"Circunferencia do circulo: {circunferencia:.2f}")
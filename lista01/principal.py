from geometria import Circulo

def main():
    raio = float(input("Digite o raio do círculo: "))
    circulo = Circulo(raio)

    area = circulo.calcular_area()
    perimetro = circulo.calcular_perimetro()

    print(f"Área do círculo: {area:.2f}")
    print(f"Perímetro do círculo: {perimetro:.2f}")

if __name__ == "__main__":
    main()
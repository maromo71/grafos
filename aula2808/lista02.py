'''
programa que recebe 05 valores do usuario
apresenta o maior e o menor ao final da 
operacao
'''

def encontrar_maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

def encontrar_menor(numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def main():
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    maior_valor = encontrar_maior(numeros)
    menor_valor = encontrar_menor(numeros)

    print(f"Vetor digitado: {numeros}")
    print(f"Maior valor: {maior_valor}")
    print(f"Menor valor: {menor_valor}")

if __name__ == "__main__":
    main()


import random
magico = random.randint(1, 1000)
cont = 0
lista = []
while True:
    if cont == 10:
        print("Suas chances terminaram")
        print("O magico era ", magico)
        break # forca a saida do while
    print()
    print("Tentativa: ", cont + 1, "de 10")
    numero = int(input("Digite o palpite: [1..1000]: "))
    lista.append(numero)
    cont += 1
    
    if numero == magico:
        print("Parabens, voce acertou!")
        break # forca a saida do while
    else:
        print("Voce errou. Tente novamente..")
        print("Palpites anteriores: ", lista)
        if numero > magico:
            print("Palpite ALTO")
        else:
            print("Palpite BAIXO")

print("Fim de jogo")
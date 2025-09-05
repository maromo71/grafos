# lista de 10 valores recebidos, filtrar uma
# lista com valores pares.
lista = []
pares = []
for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if numero % 2 == 0: # resto
        pares.append(numero)


print(lista)
print(pares )
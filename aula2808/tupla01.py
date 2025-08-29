tupla = (12, 1, 7)
maria, joao, pedro = tupla
print("Qtd da maria: ", maria)
print("Qtd do joao: ", joao)
print("Qtd do pedro: ", pedro)

print(tupla)

coordenadas = (23, 14)


x, y = coordenadas

print(x)
print(y)

graficos = [(1, 3), (3, 5), (8, 7)]
print(graficos)

# percorre o grafico e mostrar o conjunto de 3 coordenadas
for x, y in graficos:
    print(f"Coordenada x: {x} e y: {y}")
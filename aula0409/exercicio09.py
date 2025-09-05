lista1 = [7, 9, 1, 2, 11, 3, 4]
lista2 = [1, 3, 4, 7, 11]

conjunto = set(lista1)
conjunto2 = set(lista2)

interseccao = list (conjunto.intersection(conjunto2))

# ordenando os elementos comuns
interseccao.sort()
print(interseccao)
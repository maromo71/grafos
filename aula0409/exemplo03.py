conj_a = {1, 2, 3, 4, 5}
conj_b = {3, 4, 6, 7}

total = conj_a.union(conj_b)
print(total)

interseccao = conj_a.intersection(conj_b)
print(interseccao)

diferenca = conj_a.difference(conj_b)
print(diferenca)

simetrica = conj_a.symmetric_difference(conj_b)
print(simetrica)
# dois conjuntos. Uniao, interseccao e diferenca
ca = {1, 2, 3, 4, 5, 6}
cb = {1, 3, 5, 7, 9, 11}

uniao = ca.union(cb)
print(uniao)

interseccao = ca.intersection(cb)
print(interseccao)

diferenca = ca.difference(cb)
print(diferenca)

simetrica = ca.symmetric_difference(cb)
print(simetrica)
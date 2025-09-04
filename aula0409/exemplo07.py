# exemplo do for
# contagem de 0 a 10
for i in range(0, 11):
    print(i)

# pares de 0 a 50
for i in range(0, 51, 2):
    print(i)

nomes = ["ana", "carina", "tereza"]

# nao aconselhavel
for i in range(0, len(nomes)):
    print(nomes[i])

print() # pular uma linha
# aconselhavel
for nome in nomes:
    print(nome)




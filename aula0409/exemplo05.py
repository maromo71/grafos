estoque = {
    "nome": "martelo", "quantidade": 30
}
print("Chaves: ")
for chave in estoque.keys():
    print(chave)
print()
print("Valores: ")
for valor in estoque.values():
    print(valor)
print()
for chave, valor in estoque.items():
    print(f"{chave} -> {valor}")

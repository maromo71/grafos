produtos = {
    "banana": 1.67,
    "mamao": 2.67,
    "beterraba": 3.45,
    "melancia": 12.90,
    "limao": 4.80
}

media = sum(produtos.values()) / len(produtos)

print(f"Preco medio dos produtos: {media:.2f}")
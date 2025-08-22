soma = 0
mult = 1
for i in range(1, 5):
    n = float(input("Digite um numero:"))
    soma = soma + n
    mult = mult * n

print(f"A soma dos numeros é: {soma}")

media = soma / 4
print(f"A media dos numeros é: {media}")

print(f"O produto dos numeros é: {mult}")

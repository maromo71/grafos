# solicitar ao usuario que digite uma frase
# contar quantas palavras tem na frase
frase  = input("Digite uma frase: ")
print(frase.lower())

palavras = frase.split() # consideras os espaco para quebra

print(palavras)
print("Quantidade de palavras: ", len(palavras))
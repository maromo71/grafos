vogais = "aeiou"

lista_vogais = list(vogais)

print(vogais)
print(lista_vogais)

email = "prof@gmail.com"

list_email = list(email)

for letra in list_email:
    if letra == '@':
        print("Tem @ no email")
        break

list_email.remove('@')
print(list_email)
list_email.remove('.')
print(list_email)

email = "".join(list_email)
print(email)


        





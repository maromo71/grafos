from conversor import Conversor

temp = float(input("Digite a temperatura em graus celsius:"))

fahrenheit = Conversor.celsius_para_fahrenheit(temp)

print(f"A temperatura em fahrenheit é: {fahrenheit}")
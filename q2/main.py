# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

from conversor import conversor_celsius, conversor_fahrenheit

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = conversor_fahrenheit(celsius)
    print(f"{celsius} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = conversor_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
else:
    print("Opção inválida.")




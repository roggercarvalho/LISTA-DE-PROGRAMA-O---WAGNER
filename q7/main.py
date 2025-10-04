from calculadora import somar, dividir, subtrair, multiplicar

print("CALCULADORA")
operacao = input("Digite a operação: '+' '/' '-' '*': ")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

if operacao == "+":
    resultado = somar(num1, num2)

if operacao == "/":
    resultado = dividir(num1, num2)

if operacao == "-":
    resultado = subtrair(num1, num2)

if operacao == "*":
    resultado = multiplicar(num1, num2)

print(resultado)






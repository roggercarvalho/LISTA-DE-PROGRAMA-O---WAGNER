# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão

from conversor import real_para_dolar, dolar_para_real

valor = float(input("Digite o valor: "))
cotacao = float(input("Digite a cotação do dólar: "))

resultado1 = real_para_dolar(valor, cotacao)
resultado2 = dolar_para_real(valor,cotacao)


print(f"\n{valor:.2f} reais equivalem a {resultado1:.2f} dólares.")
print(f"{valor:.2f} dólares equivalem a {resultado2:.2f} reais.")

# Questão 1 - Manipulação de listas e strings


def contador_palavra(frase, palavra):

    frase_minuscula = frase.lower() #deixa minusculo
    palavra_minuscula = palavra.lower() #deixa minusculo
    palavras_frase = frase_minuscula.split() #separa por palavra por exemplo
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1

    return quantidade

# Quantidade de Palavras
# print(quantidade)

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

qtd = contador_palavra(frase, palavra)

#quantidade de palavras
print(qtd)


def contar_letras(palavra):
    count = 0
    for letra in palavra:
        count += 1
    return count
    clear(letra)

def contar_palavras(lista):
    quantidade_palavras = 0
    for palavra in lista:
        quantidade_palavras += 1
        quantidade_letras = contar_letras(palavra)
        print(f"quantidade de letras na palavra {quantidade_palavras}: {quantidade_letras}")

    print(f"quantidade de palavras na lista: {quantidade_palavras}")

# Exemplo de uso:
lista_palavras = ["oi", "tubem", "palavra", "quadro"]
contar_palavras(lista_palavras)

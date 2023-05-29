lrecebida = input("informe a letra")

def encontra_palavras(lista_palavras, letra):
    palavras_iniciadas_com_letra = []
    for palavra in lista_palavras:
        if palavra.startswith(letra):
            palavras_iniciadas_com_letra.append(palavra)
    return palavras_iniciadas_com_letra

lista = ["Donatello", "Splinter", "Michellangelo", "Rafael", "Leonardo"]
letra_inicial = lrecebida

resultado = encontra_palavras(lista, letra_inicial)


print(resultado)
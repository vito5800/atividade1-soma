def soma(indice=13, soma=0, k=0):
    """
    a cada inteiração do loop a função adiciona
    o valor de 'k' na variavel 'soma' e incrementa
    k em 1
    """
    if k < indice:
        k += 1
        soma += k
    return f"a soma é {soma}"


print(soma())

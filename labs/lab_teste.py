def triangulo(n):
    tri = []

    for i in range(n):

        if i == 0:
            tri.append([1])
        else:
            anterior = tri[-1]
            linha = [1]

            for j in range(1, len(anterior)):
                linha.append(anterior[j-1] + anterior[j])
            linha.append(1)
            tri.append(linha)

    return tri
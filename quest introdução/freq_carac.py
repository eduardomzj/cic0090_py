def frequencia(mensagem):
    if mensagem == '':
        return ''

    maior = mensagem[0]

    for c in mensagem:
        if mensagem.count(c) > mensagem.count(maior):
            maior = c

    return maior
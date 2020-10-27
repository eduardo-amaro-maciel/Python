def abreDicionario():
    """
    :return: dicionario.txt com as palavras
    """
    varTemp = list()
    with open ('dicionario.txt', 'r') as frase:
        for linha in frase.readlines():
            varTemp.append(linha.strip ('\n'))
    return varTemp


def abreArquivos(arquivo):
    """
    :param arquivo: arquivo que ira ser aberto
    :return: palavras separas em lista
    """
    palavrasArquivo = list ()
    with open (str (arquivo), 'r') as arquivoCriptografado:
        for linha in arquivoCriptografado:
            if linha.strip ('\n') != '':
                for palavra in linha.strip ('\n').split (" "):
                    palavrasArquivo.append (palavra)
    return palavrasArquivo


def decifrador(lista, senha=0):
    """
    :param lista: recebe a lista com os elementos separados
    :param senha: numeros de trocas de letras
    :return: a lista com as palavras traduzidas
    """
    varTemp = list ()
    stringTemp = ''

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for palavra in lista:
        for caracter in palavra:
            if caracter in alfabeto:
                mensagemIndex = alfabeto.index (caracter)
                stringTemp += alfabeto[(mensagemIndex + senha) % len (alfabeto)]
            else:
                stringTemp += caracter
        varTemp.append (stringTemp)
        stringTemp = ''
    return varTemp


def descobreCod(wordsLs, dictionary):
    """
    :param wordsLs: recebe a lista original do arquivo
    :param dictionary: dicionario.txt de palavras conhecidas (que é uma lista)
    :return: numeros de vezes sera deslocado cada letra
    """
    dicioProb = list ()
    maiorProb = maiorCod = 0
    for i in range(26):
        dicioProb.append(0)
    for cod in range(26):
        tempWordsLs = decifrador (wordsLs, cod)
        for palavra in tempWordsLs:
            if palavra in dictionary:
                dicioProb[cod] += 1
    for j, prob in enumerate (dicioProb):
        if prob > maiorProb:
            maiorProb = prob
            maiorCod = j
    return maiorCod


def decifradorArquivo(enderecoArq, senha):
    """
    - > ira criar um arquivo chamado "decifrado.txt" e ira sobreescrever toda vez que for execultado
    :param enderecoArq: recebe o nome do arquivo que o usuario digita
    :param senha: recebe o numero de trocas correto
    :return: no return
    """
    with open(str(enderecoArq), 'r') as arquivo:
        with open('decifrado.txt', 'w') as decifrado:
            palavrasArquivo = list()
            for linhasArquivo in arquivo:
                for palavras in linhasArquivo.split (' '):
                    palavrasArquivo.append (palavras)
            palavrasDecifradas = decifrador(palavrasArquivo, senha)
            for palav in palavrasDecifradas:
                decifrado.write(str(palav) + ' ')
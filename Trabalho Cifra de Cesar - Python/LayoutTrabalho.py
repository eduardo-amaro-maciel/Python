from time import sleep
import uteis

def lay():
    """
    -> :lay: layout do algoritimo
    :return: no return
    """
    print(f'\033[1:30:44m{"DECIFRADOR DE CESAR":_^50}\033[m')
    print(f'\033[1:33m{"BY":.^50}')
    print(f'{"GABRIEL MAFFETI DE ALMEIDA":.^50}')
    print(f'{"EDUARDO AMARO MACIEL":.^50}\033[m')
    sleep(3)

    print(f'\033[1:30:44m{"INTRUÇÕES":_^50}\033[m')

    while True:
        errorTest = False

        print ('\n1 - Digite o nome do arquivo (SEM A EXTENSÃO .txt)')
        print ('\n2 - Digite "SAIR" para fechar o programa')
        entradaUsuario = str(input("\nEntrada: ")).upper()

        if 'SAIR' in entradaUsuario:
            break
        try:
            palavras = uteis.abreArquivos(str(entradaUsuario))
        except FileNotFoundError:
            print(f'\033[1:31m{"ARQUIVO NÃO ENCONTRADO":_^50}\033[m')
            errorTest = True
        if not errorTest:
            print(f'\n\033[1:33m{"DESCOBRINDO CÓDIGO..."}\033[m')
            try:
                dicio = uteis.abreDicionario()
                codigo = uteis.descobreCod(palavras, dicio)
                print(f'O CÓDIGO É: {codigo}')
                uteis.decifradorArquivo(entradaUsuario, codigo)
            except:
                print(f'\033[1:31m{"ERRO DESCONHECIDO":_^50}\033[m')
                print(f'\033[1:31m{"TENTE NOVAMENTE":_^50}\033[m')

            # exibindo a frase completa dos arquivos
            print (f'A FRASE COMPLETA É: \n')
            with open('decifrado.txt', 'r') as textoPronto:
                print(str(textoPronto.read()))

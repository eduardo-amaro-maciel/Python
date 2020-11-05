acabou = False
vezX = True
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def imprimirTabuleiro(tabuleiro):
    print ("\n\n")
    print (tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2], sep = "")
    print ("-----")
    print (tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2], sep = "")
    print ("-----")
    print (tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2], sep = "")
    print ("\n\n")


def alguemGanhou(tabuleiro):
    for i in range (3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " ":
            print ("O jogador", tabuleiro[i][0], "ganhou!")
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " ":
            print ("O jogador", tabuleiro[0][i], "ganhou!")
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        print ("O jogador", tabuleiro[0][0], "ganhou!")
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        print ("O jogador", tabuleiro[0][2], "ganhou!")
        return True

    for i in range (3):
        for j in range (3):
            if tabuleiro[i][j] == " ":
                return False

    print ("Deu velha")
    return True


imprimirTabuleiro(tabuleiro)

while not acabou:

    while True:
        try:
            x = int (input ("Digite a linha da jogada:"))
            y = int (input ("Digite a coluna da jogada:"))

            if tabuleiro[x][y] == " ":
                if vezX:
                    tabuleiro[x][y] = "X"
                else:
                    tabuleiro[x][y] = "O"
                break
            else:
                print("Casa ocupada")
        except:
            print("Refaça a jogada")

    vezX = not vezX

    imprimirTabuleiro(tabuleiro)

    if alguemGanhou(tabuleiro):
        acabou = True
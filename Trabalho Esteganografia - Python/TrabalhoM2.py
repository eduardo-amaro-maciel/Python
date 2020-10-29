import numpy as np
import cv2 as cv
#from google.colab.patches import cv2_imshow somente para Google Colab
import matplotlib.pyplot as plt

bvr = 0 #define modo de cor do programa, 0 = azul, 1 = verde, 2 = vermelho

def bitfield(n): #passa um número e retorna binário equivalente
    return [int(digit) for digit in bin(n)[2:]]

def gerar_mensagem(mensagem): #passa string, retorna array de binários
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)

        if len(bits) < 8:
            for a in range(8-len(bits)):
                bits.insert(0,0)
        lista.append(bits)
    arr = np.array(lista)
    arr = arr.flatten()
    return arr


def converter_mensagem(saida): #passa array de binários e retorna string
    bits = np.array(saida)
    mensagem_out = ''
    bits = bits.reshape((int(len(saida)/8), 8))
    for b in bits:
        sum = 0
        for i in range(8):
            sum += b[i]*(2**(7-i))
        mensagem_out += chr(sum)
    return mensagem_out

def limpaBVR(img2): #limpa último bit da imagem (seta em zero) (recebe imagem original)
  img = img2.copy() #copia imagem original para não alterar imagem original
  for i in range(img.shape[0]):
    for j in range(img.shape[1]): #navega pelos pixels da imagem
      if img[i, j, bvr] % 2 != 0: #caso o número da cor não seja par
        img[i, j, bvr] = img[i, j, bvr] - 1 #diminui 1, tornando par (caso seja 0, continua 0) (caso seja 1, vira 0) (caso seja 255, vira 254)
  return img #retorna imagem limpa

def gravaMsg(img2, msg): #grava mensagem em binário no último bit da imagem, já limpa (recebe imagem limpa, e mensagem em binário)
  img = img2.copy() #copia a imagem original para evitar alterações
  contador = 0 #inicia contador
  for i in range(img.shape[0]):
    for j in range(img.shape[1]): #navega pela imagem
      if msg[contador] == 1: #se na mensagem convertida em binário, na posição onde o contador está houver 1
        img[i, j, bvr] = img[i, j, bvr] + 1 #transforma pixel em pixel ímpar
      contador += 1 #soma um ao contador
      if contador >= len(msg): #caso contador lote, para laço de repetição
        break
    if contador >= len(msg): #caso contador lote, para laço de repetição
      break
  return img #retorna imagem codificada com mensagem

def puxaUltmBit(img2): #retorna ultimo bit da cor azul da imagem (recebe imagem codificada)
  img = img2.copy() #copia a imagem códificada original, para não a alterar
  textoBin = [] #inicia lista de binários
  for i in range(img.shape[0]):
    for j in range(img.shape[1]): #navega pela imagem
      if img[i, j, bvr] % 2 == 0: #caso seja par
        textoBin.append(int (0)) #adiciona zero
      else: #caso contrário
        textoBin.append(int (1)) #adiciona um 
  return textoBin #retorna lista de binários com texto

def deletaLixoMsg(msg): #retorna mensagem limpa
  msgLimpa = '' #inicia string
  for letra in msg: #itera cada letra na mensagem
    if letra == chr(3): #se o caracter da ETX (end of text, número 3)
      break #para
    else: #se não, adiciona a letra
      msgLimpa = msgLimpa + letra
  return msgLimpa #volta a mensagem fltrada/limpa

while True: #programa principal
  modo = input('Seja Bem-Vindo!!!\n1-Gravar mensagem em um arquivo cifrado.png\n2-Decifrar mensagem e salvar em decifrado.txt\nDigite o modo de operação:')
  if modo == '1': #gravar mensagem
    nomeImg = str (input('Digite o nome do arquivo a ser lido (com extensão): '))
    imgOriginal = cv.imread(nomeImg) #lê imagem original
    imgLimpa = limpaBVR(imgOriginal) #transforma a quantidade de azul/vermelho na imagem em par
    msgUsr = gerar_mensagem(str (input('Digite a frase a ser gravada na imagem: ') + chr(3))) #entra mensagem, marca fim de texto e converte para binário
    imgCifrada = gravaMsg(imgLimpa, msgUsr) #grava mensagem
    cv.imwrite('cifrado.png', imgCifrada) #grava arqivo cifrado.png com imagem
    print('Imagem gravada com sucesso!')
    break #fim do modo 1
  elif modo == '2': #ler mensagem
    nomeImg = str (input('Digite o nome do arquivo a ser lido (com extensão): '))
    imgOriginal = cv.imread(nomeImg) #lê imagem criptografada
    msgCifrada = puxaUltmBit(imgOriginal) #salva o último bit de cada quantidade de cor azul/vermelha da imagem
    msgDecifrada = converter_mensagem(msgCifrada) #converte binário para string
    msgLimpa = deletaLixoMsg(msgDecifrada) #limpa lixo (caracter null) da imagem
    print(msgLimpa) #exibe mensagem
    with open('decifrado.txt', 'w') as arquivo: #salva mensagem em .txt
      arquivo.write(msgLimpa)
    break #fim do modo 2
  else:
    print('Por favor selecione uma opção válida!')

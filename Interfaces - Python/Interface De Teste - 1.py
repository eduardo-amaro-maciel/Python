from tkinter import *

janela = Tk()

lista = []
texto1 = StringVar()
texto2 = StringVar()
texto3 = StringVar()
texto4 = StringVar()


#--------------------- PROCESSAMENTO DO COMANDO ------
def click_bt1():

    lista.append(int(et1.get()))
    lista.append(int(et2.get()))
    lista.append(int(et3.get()))
    lista.append(int(et4.get()))
    txt1.delete(0.0, 'end')
    for i in lista:
        if i % 2 == 0:
            txt1.insert(0.0, f'{i} ')
    txt1.insert(0.0, '- Os valores pares digitados foram: ')
    if 3 in lista:
        txt1.insert(0.0, f'- O número 3 apareceu na {lista.index(3)+1} posição.\n')
    else:
        txt1.insert(0.0,'- O número 3 não apareceu na lista.\n')

    txt1.insert(0.0, f'- Você digitou o número "9" {lista.count(9)} vezes.\n')
    texto1.set(str(''))
    texto2.set(str(''))
    texto3.set(str(''))
    texto4.set(str(''))
    print(lista)
#------------------------------------------------------


#---------------INSERÇÃO DOS WIDGETS ---------------
lb1 = Label(janela, text='Digite o primeiro número: ')
lb1.grid(row=0,column=0, stick=W)
lb2 = Label(janela, text='Digite o segundo número: ')
lb2.grid(row=1,column=0, stick=W)
lb3 = Label(janela, text='Digite o terceiro número: ')
lb3.grid(row=2,column=0, stick=W)
lb4 = Label(janela, text='Digite o quarto número: ')
lb4.grid(row=3,column=0, stick=W)

et1 = Entry(janela, textvariable=texto1, width=5)
et1.grid(row=0,column=1,sticky=E)
et2 = Entry(janela, textvariable=texto2, width=5)
et2.grid(row=1,column=1,sticky=E)
et3 = Entry(janela, textvariable=texto3, width=5)
et3.grid(row=2,column=1,sticky=E)
et4 = Entry(janela, textvariable=texto4, width=5)
et4.grid(row=3,column=1,sticky=E)

bt1 = Button(janela,text='PROCESSAR', font=('arialblack',11,'bold'),command=click_bt1)
bt1.grid(row=0,column=2,rowspan=4)

txt1 = Text(janela,width=40,height=10,bd=5)
txt1.grid(row=5,column=0,columnspan=3)
#----------------------------------------------------------------------


#------------------- DIMENSIONAMENTO E CENTRALIZAÇÃO DA JANELA --------
janela.title('Exercicio - Ex075')
janela_width = 330
janela_height = 260

scream_width = janela.winfo_screenwidth()
scream_height = janela.winfo_screenheight()

cord_x = int((scream_width/2) - (janela_width/2))
cord_y = int((scream_height/2) - (janela_height/2))

janela.geometry(f'{janela_width}x{janela_height}+{cord_x}+{cord_y}')
#---------------------------------------------------------------------

janela.mainloop()
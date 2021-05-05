import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox 
import sys 




paisEscolhido = []
def verificaSelecao():
    paisEscolhido.append(str(escolhePais.get()))
    janelaPais.quit() 
    confirma.config(state = 'disabled') 
    escolhePais.config(state = 'disabled')
    info.config(state = 'normal')
    textoPais.config(text = 'País selecionado,\ngráficos em exibição')




def sair(): 
    sys.exit(0)




def informacoes(): 
    
    janelaDados = tk.Tk()

    janelaDados.title("Informações - Debug")
    janelaDados.geometry('1120x480')
    

    f = tk.Frame(janelaDados)
    f.place(x=10, y=10)
    scrollbar = tk.Scrollbar(f)

    textoInfo = tk.Text(
        f, 
        bg = '#FFFFFF', 
        width=120, 
        font = 'Consolas',  
        yscrollcommand = scrollbar.set
    )

    textoInfo.tag_configure(
        "center", 
        justify='center'
    )

    scrollbar.config(command = textoInfo.yview)

    textoInfo.insert(
        'insert', 
        str('Formato do DataFrame: ' + str(df.shape) + '\n'), 
        'center'
    ) 
        
    textoInfo.insert(
        'insert', 
        str( df.head())
    )
    
    textoInfo.insert(
        'insert', 
        str("\nFormato do DataFrame Escolhido: " + str(paisEscolhido[-1]) + str(df_escolhido.shape) + '\n' ), 
        'center'
    ) 
    
    textoInfo.insert(
        'insert', 
        str( df_escolhido.head())
    )
    
    textoInfo.insert(
        'insert', 
        str('\n--> Mundial:' + str(df.isnull().sum()) + "\n" + "--." * 10 + "\n")
    )

    textoInfo.insert(
        'insert', 
        str('\n--> ' + str(paisEscolhido[-1]) + ':' + str(df_escolhido.isnull().sum()) + "\n" + "--." * 10 + "\n")
    )
    
    textoInfo.insert(
        'insert', 
        str(table.head())
    )

    textoInfo.config(state = 'disabled')
    scrollbar.pack(side='right', fill='y')
    textoInfo.pack()




def separarPaises():

    col_list = ["country"]
    try:
        df = pd.read_csv("master.csv", usecols=col_list)
    except:
        tk.messagebox.showerror(
            title = 'Arquivo "master.csv" não encontrado', 
            message = 'Verifique se "master.csv" está localizado na raiz do arquivo.'
        )
        sair()


    arr = df.to_numpy()
    paises = []
    flattened = []

    for pais in arr:
        if pais not in paises:
            paises.append(pais)

    for sublist in paises:
        for val in sublist:
            flattened.append(val) 
    return flattened




def retornaAnosFaltantes(dframe, paisSelecionado):
        
    anosFaltantes = []
    anosPresentes = []
    df = dframe
    filtro = dframe['country'].str.contains(paisSelecionado)
    separaPais = df[filtro] 

    for i in separaPais['year']:
        for j in range(1985, 2017):
            if i == j:
                if i not in anosPresentes:
                    anosPresentes.append(i)

    for i in range(1985, 2017):
        if i not in anosPresentes:
            anosFaltantes.append(i)
    return anosFaltantes




def limpaAnosFaltantes(anosFaltantes):
    
    for ano in anosFaltantes:
        suicides_world_mean.drop(ano, inplace=True)




try:   
    df = pd.read_csv('master.csv')
except:
    tk.messagebox.showerror(
        title = 'Arquivo "master.csv" não encontrado', 
        message = 'Arquivo do banco de dados não encontrado, verifique se ele está localizado na raiz do arquivo executável.'
    )
    sair()

janelaPais = tk.Tk()

try:
    janelaPais.iconbitmap('icon.ico')
except:
    tk.messagebox.showwarning(
        title = 'Arquivo "icon.ico" não encontrado', 
        message = 'Arquivo de ícone não na pasta raiz.'
    )


janelaPais.title('Setembro Amarelo')
janelaPais.geometry('300x250')
janelaPais.protocol('WM_DELETE_WINDOW', sair)


textoPais = tk.Label(
    master = janelaPais, 
    text = 'Selecione o país a ser analisado:', 
    font = '12'
)

textoPais.place(
    relx=0.5, 
    rely=0.3, 
    anchor='center'
)

escolhePais = ttk.Combobox(
    janelaPais,
    values = separarPaises(),
    state = 'readonly'
)

escolhePais.current(15)

escolhePais.place(
    relx=0.5, 
    rely=0.5, 
    anchor='center'
)

confirma = ttk.Button(
    janelaPais, 
    text = 'Confirma', 
    command = verificaSelecao, 
    state = 'active'
)

confirma.place(
    relx=0.5, 
    rely=0.6, 
    anchor='center'
)

info = ttk.Button(
    janelaPais, 
    text = 'Informações', 
    command = informacoes, 
    state = 'disabled'
)

info.place(
    relx=0.5, 
    rely=0.7, 
    anchor='center'
)

sair = ttk.Button(
    janelaPais, 
    text = 'Sair', 
    command = sair
)

sair.place(
    relx=0.5, 
    rely=0.9, 
    anchor='center'
)

janelaPais.mainloop() 

df_escolhido = df[df.country == str(paisEscolhido[-1])].copy()

years = df_escolhido.year.unique()    
suicides_brasil_mean = df_escolhido.groupby('year')['suicides/100k pop'].mean()
suicides_world_mean = df.groupby('year')['suicides/100k pop'].mean()


limpaAnosFaltantes(retornaAnosFaltantes(df, paisEscolhido[-1]))

plt.figure(
    num = 'Gráfico de linhas', 
    figsize=(6,5), dpi=100
)

sns.lineplot(
    x=years, 
    y=suicides_brasil_mean, 
    label=str(paisEscolhido[-1])
)

sns.lineplot(
    x=years, 
    y=suicides_world_mean, 
    label='Mundo'
)

plt.legend(title="Taxa de suicídio")
plt.plot()

table = pd.pivot_table(
    df_escolhido, 
    values='suicides_no', 
    index=['year'], 
    columns=['age']
)

column_order = [
    '5-14 years', 
    '15-24 years', 
    '25-34 years', 
    '35-54 years', 
    '55-74 years', 
    '75+ years'
]

table = table.reindex(
    column_order, 
    axis=1
)

table.plot.bar(
    stacked=True, 
    figsize=(16,8)
)

plt.legend(title="Idade")
plt.plot()

homens_mulheres = df_escolhido.groupby('sex').suicides_no.sum() / df_escolhido.groupby('sex').suicides_no.sum().sum()

plt.figure(num = 'Gráfico de Pizza')

plt.pie(
    homens_mulheres, 
    labels=['Mulheres', 'Homens'], 
    autopct='%1.2f%%', 
    shadow=True
)

plt.plot()
plt.show()
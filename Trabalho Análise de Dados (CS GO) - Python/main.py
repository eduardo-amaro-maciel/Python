import matplotlib.pyplot as plt
import pandas as pd


csgo = pd.read_csv('CSGOComplete.csv')

csgo = csgo.rename(columns = {'Year':'Ano', 'Map':'Mapa', 'Result':'Resultados'})


filtro2015 = csgo[csgo['Ano'] == 2015]
Result = filtro2015['Resultados'].value_counts()


listaValoresResultados = list()
for valor in Result:
    listaValoresResultados.append(valor)


TipoDeResultado = list()
for tipo, i in filtro2015.groupby(by = 'Resultados'):
    TipoDeResultado.append(tipo)


plt.bar(TipoDeResultado, listaValoresResultados, color = ['yellow','lime','cyan'])
plt.title('Average wins, losses and draws in 2015 \n GAME - CS GO')
plt.xlabel('Types of results')
plt.ylabel('Number of wins, losses and draws')
plt.show()


contMapaJogado = filtro2015['Mapa'].value_counts()


x = contMapaJogado.keys()
y = contMapaJogado.values

plt.barh(x, y, color=['red','green','black','yellow','pink','lime','cyan','magenta'])
plt.yticks(rotation=69)
plt.title('Most played maps in 2015 \n GAME - CS GO')
plt.ylabel('Game Maps')
plt.xlabel('Number of times played')

plt.show()

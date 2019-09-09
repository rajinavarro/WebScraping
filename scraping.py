import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Estabelecendo conexão com o servidor
req = requests.get('https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/')
if req.status_code == 200:
    #print('Requisição bem sucedida!!')
    content = req.content

#Extraindo tabelas
soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all(name = 'div', attrs={'class':'col-main'})

#Acessando tabelas como String via Pandas
tabel_str = str(table)

df = pd.read_html(tabel_str)[0]
#df.info()

lista = []
for i in df['P']:
    lista.append(i)
lista2 = []

for i in range(len(df['Times.2'])):
    a = ''
    a = df['Times.2'][i]
    a = a[:-3]
    df['Times.2'][i] = a

    

df.plot(kind='bar', x='Times.2', y='P')
plt.show()

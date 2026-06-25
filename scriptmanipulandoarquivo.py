# !pip -q install plotly --upgrade
#!pip -q install yellowbrick
#biblioteca pra trabalhar com csv
import pandas as pd
# biblioteca para manipulação de matrizes e arrays multidimensionais
import numpy as np
# biblioteca de visualização de graficos
import seaborn as sns
#biblioteca de visualização de graficos
import matplotlib.pyplot as plt
#grafico dinamico
import plotly.express as px
#importar arquivo no google scholar do drive
'''
from google.colab import drive
drive.mount('/content/drive') '''

#abre a base de dados
base_credit = pd.read_csv('E:/dowloads/curso ia/archive/credit_risk_dataset.csv')

#arquivo lido
#print(base_credit)

#arquivo lido só os 10 primeiros
#print(base_credit.head(10))

#arquivo lido só os 8 ultimos
#print(base_credit.tail(8))

#estatiticas dos dados
#print(base_credit.describe())

#mostra a base mas filtrando na base person_income que for maior ou igual ao valor
#print(base_credit[base_credit['person_income'] >= 69995.685578])

#mostrando base filtrada com dados onde o loan_percent_income é menor ou igual ao valor
#print(base_credit[base_credit['loan_percent_income'] <= 1.377630])

#conta quantas classes tem na coluna e quantia total de cada uma
#print(np.unique(base_credit['cb_person_default_on_file'], return_counts=True))

#grafico contando os valores no atributo da classe mostrada
#sns.countplot(x = base_credit['cb_person_default_on_file']);
#plt.show()

#plt.hist(x = base_credit['person_age']);
#plt.show()

#plt.hist(x = base_credit['person_income']);
#plt.show()

#plt.hist(x = base_credit['loan_amnt']);
#plt.show()
#gera graficos correlacionando da base de dados, os atributos, divididos por outro atributo
grafico = px.scatter_matrix(base_credit, dimensions=['person_age','loan_percent_income','loan_amnt'], color = 'loan_status')
grafico.show()



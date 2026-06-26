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
#grafico = px.scatter_matrix(base_credit, dimensions=['person_age','loan_percent_income','loan_amnt'], color = 'loan_status')
#grafico.show()

#========================TRATAMENTO DE VALORES  INCONSISTENTES
#filtrando valores abaixo de 0
#base_credit.loc[base_credit['age'] < 0]
#base_credit[base_credit['age'] < 0]

# Apagar a coluna inteira (de todos os registros da base de dados)
#base_credit2 = base_credit.drop('person_age', axis = 1)
#print(base_credit2)

#index das linhas da base, traz o numero inicial, final e de quanto em quanto a tabela traz
#print(base_credit.index)
#localiza o index das linhas onde idade é menor que 0
#base_credit[base_credit['age'] < 0].index


# Apagar somente os registros com valores inconsistentes
#base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
#base_credit3
#base_credit3.loc[base_credit3['age'] < 0]

# Preencher os valores inconsistente manualmente
# Prencher a média
#base_credit.mean()
#base_credit['age'].mean()
#base_credit['age'][base_credit['age'] > 0].mean()
#base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92
#base_credit.loc[base_credit['age'] < 0]
#base_credit.head(27)

#============= TRATAMENTO DE DADOS FALTANTES
#mostra quantos atributos estão nulls
#base_credit.isnull()
#soma a quantidade de  nulls por coluna
#base_credit.isnull().sum()
# trazer os valores das linhas com idades nulas
#print(base_credit.loc[pd.isnull(base_credit['person_age'])])
#preencher todas as linhas da coluna age que estão vazias com a media dos valores
#base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)
#pega os valores de linhas especificas com base nos ids dos clientes
#base_credit.loc[(base_credit['clientid'] == 29) | (base_credit['clientid'] == 31) | (base_credit['clientid'] == 32)]
#mesma coisa mas em um vetor, pega as linhas dos ids dos clientes que tiverem na lista
#base_credit.loc[base_credit['clientid'].isin([29, 31, 32])]
#ver as linhas que estão nulas da coluna age
#base_credit.loc[pd.isnull(base_credit['age'])]

#===================separação para dados os previsores e classe==============
#X_credit é previsor e y_credit é classe
#puxando os valores, [:(todos os valores,ta coluna 1 até o 4(busca do 1 até o 3))], values converte pro formato do numpy
#X_credit = base_credit.iloc[:, 1:4].values
#X_credit
#ver o tipo da variavel, deve ser tipo numpy
#type(X_credit)
#todos os valores, e a ultima coluna
#y_credit = base_credit.iloc[:, 4].values
#y_credit
#type(y_credit)

#=================Escalonamento  dos Valores================
#previsores
#0 renda, 1 idade, 2 divida
#X_credit
#apresentar o minimo da renda, menor idade e  menor divida
#X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
#apresentar o maximo da renda, maior idade e maior divida
#X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()

#biblioteca de aprendizagem de maquina no python, standardScaler é oq aplica a padronização
#from sklearn.preprocessing import StandardScaler
#criando variavel standardScaler
#scaler_credit = StandardScaler()
#chamamos o scaler com a fit_transform que se encaixa nos dados e faz a transformação recebendo X_credit(a base)
#X_credit = scaler_credit.fit_transform(X_credit)
#verificando após o codigo
#X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
#X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()
#X_credit

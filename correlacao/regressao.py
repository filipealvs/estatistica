# 1. Importação das libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install scikit-learn
from sklearn.linear_model import LinearRegression

# 2. Carregamento e preparação dos dados
EXPOSICAO_ALGODAO = 'data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

# Gráfico de DISPERSÃO
# dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
# plt.show()

# 3. Configuração e treinamento do modelo
# Define a variáve preditora (independente), que é
# a Exposure e a variável de resultado que é o PEFR
predictors = ['Exposure']
outcome = 'PEFR'
# Instanciar o modelo
model = LinearRegression()
# Etapa d etreinamento
model.fit(dataframe[predictors], dataframe[outcome])

# 4. Exibição dos Coeficiente
# intercepto
print(f'Intercepto: {model.intercept_:.3f}')
# Coeficiente angular
print(f'Coeficiente Angular: {model.coef_[0]}')

# 5. Geração do gráfico
fig, (reg) = plt.subplots(1, 1, figsize=(4, 4))
# Gráfico regreção
reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)
plt.tight_layout()
plt.show()
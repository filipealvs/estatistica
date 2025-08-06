import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data\sp500_data.csv.gz'
df = pd.read_csv(data)
print(df.head())

## RMOVER COLUNAS ESPECIFICA
df = df.drop(columns=['ADS'])
print(df.head())

# RENOMEAR CLUNAS ESPECIFICAS
df = df.rename(columns={'Unnamed: 0': 'Data'})
print(df.head())
#  TRANSFORMAR O CAMPO  DATA PARA DATETIME E SETTAR ELE COMO INDICE
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
print(df.head())

# ENCTORAR A MAIOR E MENOR DATA
data_inicio = df.index.min()
data_fim = df.index.max() 
print(f"Quantidade de variações coletada: {len(df)}")
print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y')} à {data_fim.strftime('%d/%m/%Y')}")

ativo = 'IBM'

# ENCONTRAR O VALOR MÁXIMO E O MÍNIMO DO ATIVO
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print("-" * 30)
print(f"Ativo: {ativo}")
print(f"Maior variação diária: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")
print(f"Menor variação diária: {menor_valor:.4f}")
print(f"Ocorreu no dia: {data_menor.strftime('%d/%m/%Y')}")

#MEDIDAS DE TENDÊNCIA CENTRAL
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()
print(f"Médidas de tendências Central para {ativo}:")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
if(len(moda) >0):
    print(f"Modas: {moda}")
else:
    print(f"O ativo {ativo} é amodal")

df_frequencia = df[ativo].value_counts()
print(df_frequencia.head())
print("-" * 30)

#ESTIMATIVAS DE VARIABILIDADE
desvio_absoluto = np.abs(df[ativo] - media)
desvio_absoluto_medio = np.mean(desvio_absoluto)
variancia = np.var(df[ativo], ddof=1)
desvio_padrao = np.std(df[ativo], ddof=1)
print(f"Estimativas de variabilidade para: {ativo}")
print(f"Desvio Absoluto médio: {desvio_absoluto_medio}")
print(f"Variância: {variancia:.4f}")
print(f"Desvio Padrão: {desvio_padrao:.4f}")

#GRÁFICOS
serie_as_dataframe = pd.DataFrame(df[ativo])

# Histograma
plt.figure() # Cria a primeira figura (janela)
sns.histplot(data = serie_as_dataframe)
plt.xlabel("Variação percentual diária")
plt.ylabel("Ocorrências")
plt.title("Histograma")

# Boxplot
plt.figure() # Cria a segunda figura (janela)
sns.boxplot(data = serie_as_dataframe)
plt.ylabel("Variação do percentual Diária")
plt.title("Boxplot")

# Desidade
plt.figure()
sns.kdeplot(data = serie_as_dataframe)
plt.xlabel("Variação percentual diária")
plt.ylabel("Ocorrências")
plt.title("Densidade")


plt.show()



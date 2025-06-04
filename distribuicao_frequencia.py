import pandas as pd
import numpy as np
import math

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"--- Análise Estatística para: {nome_do_conjunto} ---")

    rol = sorted(dados_brutos)
    print("\n1. Rol (Dados Ordenados):")
    print(f" {rol}")

    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f" n = {n}")

    x_min = rol[0]
    x_max = rol[-1]
    print("\n3. Valor Máximo e Mínimo:")
    print(f" valor min: {x_min}")
    print(f" valor max: {x_max}")

    at = x_max - x_min
    print("\n4. Amplitude Total (AT): ")
    print(f" AT = {at:.2f}")

    k = math.ceil(math.sqrt(n))
    print("\n5. Número de Classes (K):")
    print(f"K = {k}")
    
    h = at / k
    print("\n6. Amplitude das Classes (h):")
    print(f"h = {h}")
    
    classes = []
    frequencias_absolutas = []
    pontos_medios = []
    frequencias_relativas_dec = []
    frequencias_relativas_perc = []
    frequencias_absolutas_acum = []

    frequencia_abs_acum = 0
    limite_inferior = x_min
    for i in range(k):
        limite_superior = limite_inferior + h
        classes.append(f"[{limite_inferior:.2f} --| {limite_superior:.2f}]")
        frequencia_absoluta = len([x for x in rol if limite_inferior <= x < limite_superior])
        frequencias_absolutas.append(frequencia_absoluta)
        pontos_medios.append((limite_inferior + limite_superior) / 2)
        frequencias_relativas_dec.append(frequencia_absoluta / n)
        frequencia_abs_acum += frequencia_absoluta
        frequencias_absolutas_acum.append(frequencia_abs_acum)
        frequencias_relativas_perc.append((frequencia_absoluta / n) * 100)
        limite_inferior = limite_superior

    df_frequencia = pd.DataFrame({
        'Classe': classes,
        'Ponto Médio': pontos_medios,
        'Frequência Absoluta': frequencias_absolutas,
        'Frequência Relativa Decimal': frequencias_relativas_dec,
        'Frequência Relativa Percentual (%)': frequencias_relativas_perc,
        'Frequência Absoluta Acumulada': frequencias_absolutas_acum
    })

    df_frequencia.loc['Total'] = [
        'Total',
        np.nan,
        df_frequencia['Frequência Absoluta'].sum(),
        df_frequencia['Frequência Relativa Decimal'].sum(),
        df_frequencia['Frequência Relativa Percentual (%)'].sum(),
        np.nan
    ]

    return df_frequencia

# Teste com os dados
dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "Idades dos Alunos")
print(df_idades.to_string(index=False))

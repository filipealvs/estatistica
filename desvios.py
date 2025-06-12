import pandas as pd
import numpy as np
from faker import Faker

# Instância do Faker para gerar nomes
fake = Faker('pt_BR')

# condições dos dados [População]
media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc=media_notas, scale=desvio_padrao_notas, size=num_alunos)
print(f"notas random: {notas}")
# limita as notas entre 0 a 100
# o que for menor que 0 vira  e o que é maior que 100 vira 100
notas = np.clip(notas, 0, 100)

# -- Cálculos das Medidas -- 
# 1. Média
media = np.mean(notas)
# 2 . Mediana
mediana = np.median(notas)
# 3. Desvio (Simples)
# ex. 80(média) - 70(média) = 10(desvio)
desvios = notas - media
# 4. Desvio Absoluto
# Ex. 60(nota) - 70(media) = |10|(desvio)
desvios_aboslutos = np.abs(notas - media)
# 5. Variância Individual
# Ex. 80(nota) - 70(media) = 10 * 10 = 100(variância)
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof=1) # para variância amostral (n-1)
# 6. Desvio Padrão
# Ex. 
devio_padrao = np.std(notas)
# 7. Desvio Absolut  (Mediana)
desvios_abs_em_relacao_mediana_individuais = np.abs(notas - mediana)




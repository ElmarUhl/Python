import pandas as pd

# Arquivo csv não aceita espaço antes de ano
df = pd.read_csv('carros.csv')

ano = df[['ano']].values

print(ano)

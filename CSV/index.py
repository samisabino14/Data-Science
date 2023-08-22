import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)

#função para remover os NaNs. axis=0 significa que queremos remover todas as linhas que possuem um valor NaN:
health_data.dropna(axis=0, inplace=True)

print("\n\n============================================================================================\n\n")

#função para mostrar apenas as 5 linhas principais:
print(health_data.head())

print("\n\n============================================================================================\n\n")

print(health_data)
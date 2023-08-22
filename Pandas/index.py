import pandas as pd

my_dataset = {
    'cars': ["BMW", "Mercedes", "Volvo", "Ford"],
    'passings': [8, 9, 10, 20]
}

result = pd.DataFrame(my_dataset)

rows_numbers = result.shape[0]
cols_numbers = result.shape[1]

print("Número de linhas:", cols_numbers)
print("Número de colunas:", rows_numbers)
print("\n")
print(result)

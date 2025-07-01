import pandas as pd

# Загрузка данных из CSV-файла
file_path = 'monthly_averages_tensei.csv'
data = pd.read_csv(file_path)


# Save the monthly averages to a new CSV file
output_path = 'monthly_averages_tensei1.csv'
data.to_csv(output_path, index=False, header=['Month', 'Average Value'])

output_path

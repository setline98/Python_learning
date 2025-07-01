import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data1 = pd.read_csv('monthly_averages_rezero1.csv')
data2 = pd.read_csv('monthly_averages_stone1.csv')
data3 = pd.read_csv('monthly_averages_tensei1.csv')

data1['Month'] = pd.to_datetime(data1['Month'])
data2['Month'] = pd.to_datetime(data2['Month'])
data3['Month'] = pd.to_datetime(data3['Month'])

plt.figure(figsize=(12, 6))

plt.plot(data1['Month'], data1['Average Value'], marker='o', color='red', label='Re:Zero')
plt.plot(data2['Month'], data2['Average Value'], marker='o', color='green', label='Dr.Stone')
plt.plot(data3['Month'], data3['Average Value'], marker='o', color='blue', label='Mushoku Tensei')

plt.ylim(0, 100)

plt.xlabel('Дата', fontsize=12)
plt.ylabel('Количество запросов', fontsize=12)
plt.title('Зависимость количества запросов от даты', fontsize=14)
plt.grid(True)

plt.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

plt.xticks(rotation=45)

plt.show()

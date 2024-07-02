import pandas as pd

# Загрузка данных
data = pd.read_csv("dz.csv")

# Печать информации о данных
print(data.info())

# Группировка данных по столбцу 'City' и вычисление среднего значения для столбца 'Salary'
group = data.groupby('City')['Salary'].mean()

# Печать результата
print(group)


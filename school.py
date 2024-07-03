import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла
df = pd.read_csv('school.csv')

# Печать первых нескольких строк DataFrame, чтобы убедиться, что данные загружены правильно
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)

print("Средние оценки по каждому предмету:")
print(mean_scores)

# Визуализация средних оценок по каждому предмету
mean_scores.plot(kind='bar', title='Средние оценки по предметам')
plt.xlabel('Предмет')
plt.ylabel('Средняя оценка')
plt.show()

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("Медианные оценки по каждому предмету:")
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)
print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")

# Вычисление IQR для оценок по математике
IQR_math = Q3_math - Q1_math
print(f"IQR для оценок по математике: {IQR_math}")

# Вычисление стандартного отклонения по каждому предмету
std_dev_scores = df.std(numeric_only=True)
print("Стандартное отклонение по каждому предмету:")
print(std_dev_scores)

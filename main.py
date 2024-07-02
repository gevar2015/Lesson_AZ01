import pandas as pd
data = pd.read_csv("mobil_mesin_harga.csv")
# Создаем группы по мощности двигателя
group1 = data[data['KekuatanMesin'] <= 120]
group2 = data[(data['KekuatanMesin'] >= 120) & (data['KekuatanMesin'] < 160)]
group3 = data[data['KekuatanMesin'] >= 160]

# Рассчитываем среднюю мощность двигателя по группе
mean_group1 = group1.mean()
mean_group2 = group2.mean()
mean_group3 = group3.mean()

# Комбинируем результаты рассчета средней цены по группам для вывода в таблицу
results = pd.DataFrame({
    'Group': ['<= 120', '120 <= x < 160', '>= 160'],
    'Mean Engine Power': [mean_group1['KekuatanMesin'], mean_group2['KekuatanMesin'], mean_group3['KekuatanMesin']],
    'Mean Price': [mean_group1['Harga'], mean_group2['Harga'], mean_group3['Harga']]
})

print(results)


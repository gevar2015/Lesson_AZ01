# Необходимо спарсить цены на диваны из категории "пряьые диваны" с сайта https://www.divan.ru/category/pramye-divany в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализируем браузер
driver = webdriver.Chrome()

# URL страницы, которую будем парсить
url = 'https://www.divan.ru/category/pramye-divany'
# Открываем веб страницу
driver.get(url)
# Даем 5 секунд на прогрузку всей страницы
time.sleep(5)

# Находим товары на странице
products = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

# Список для хранения данных
parsed_data = []

# Парсинг данных с использованием try-except для обработки ошибок
for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = product.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue
    parsed_data.append([name, price])

# Закрываем браузер
driver.quit()

# Сохранение данных в CSV файл
with open('sofas_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование дивана', 'Цена дивана'])
    writer.writerows(parsed_data)

print("Парсинг завершен, данные сохранены в sofas_prices.csv")
import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('sofas_prices.csv')

# Удаление символа "₽" и преобразование в числовой тип данных
df['Цена дивана'] = df['Цена дивана'].str.replace('руб.', '').str.replace(' ', '').astype(float)

# Сохранение обработанных данных в новый CSV файл
df.to_csv('processed_sofas_prices.csv', index=False)

print("Обработка завершена, данные сохранены в processed_sofas_prices.csv")

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка обработанных данных из CSV файла
df = pd.read_csv('processed_sofas_prices.csv')

# Расчет средней цены
average_price = df['Цена дивана'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} рублей")

# Построение гистограммы для цен
plt.figure(figsize=(10, 6))
plt.hist(df['Цена дивана'], bins=20, edgecolor='k', alpha=0.7)
plt.title('Распределение цен на диваны')
plt.xlabel('Цена дивана (в рублях)')
plt.ylabel('Количество')
plt.grid(True)

# Добавление вертикальной линии для средней цены
plt.axvline(average_price, color='r', linestyle='dashed', linewidth=1)
plt.text(average_price, plt.ylim()[1]*0.9, f'Средняя цена: {average_price:.2f} руб.', color = 'r')

plt.show()
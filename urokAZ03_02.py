import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)
y = np.random.rand(50)

# Создание диаграммы рассеяния
plt.scatter(x, y)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Показ диаграммы
plt.show()
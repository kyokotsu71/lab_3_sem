import numpy as np

arr = np.random.normal(size=(10, 4))
print(arr)
avg = np.average(arr)
max_el = np.max(arr)
min_el = np.min(arr)
std = np.std(arr)
five_str = arr[:5]
print(f'Минимальное значение: {min_el}\n'
      f'Максимальное значение: {max_el}\n'
      f'Среднее значение: {avg}\n'
      f'Стандартное отклонение: {std}\n'
      f'Первые 5 строк: {five_str}')

import numpy as np
matrix = np.loadtxt('input.txt', delimiter=',')
sum_el = np.sum(matrix)
max_el = np.max(matrix)
min_el = np.min(matrix)

print(f'Сумма: {sum_el}, Максимальный: {max_el}, Минимальный: {min_el}')
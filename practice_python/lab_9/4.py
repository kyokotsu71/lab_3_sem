import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
num = np.where(x[:-1] == 0)[0]
max_element = np.max(x[num + 1])
print(max_element)

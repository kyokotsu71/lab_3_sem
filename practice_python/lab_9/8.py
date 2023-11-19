import numpy as np

arr = [0, 1, 2, 0, 0, 4, 0, 6, 9]
nonzero = np.nonzero(arr)
print(*nonzero)

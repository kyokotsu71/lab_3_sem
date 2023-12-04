import numpy as np
import matplotlib.pyplot as plt

mid = 0
std = 1
size = 10000

samples = np.random.normal(mid, std, size)
plt.hist(samples, bins=30, density=True)
plt.show()

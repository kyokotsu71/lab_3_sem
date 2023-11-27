import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

degrees = range(1, 8)

figure, axes = plt.subplots()

for degree in degrees:
    x = np.linspace(-1, 1, 100)
    y = legendre(degree)(x)
    axes.plot(x, y, label=f'n = {degree}')

axes.set_title('Полиномы Лежандра')
axes.legend()
plt.show()

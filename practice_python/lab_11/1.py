import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 1, 1000, endpoint=False)
wave = signal.square(2 * np.pi * 10 * t)

plt.plot(t, wave)
plt.show()
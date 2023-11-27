import numpy as np
import matplotlib.pyplot as plt

arr = [(3, 2), (3, 4), (5, 4), (5, 6)]

figure, axes = plt.subplots(2, 2, figsize=(10, 10))

for i, (freq_x, freq_y) in enumerate(arr):
    ax = axes[i // 2, i % 2]
    t = np.linspace(0, 2 * np.pi, 10000)
    x = np.sin(freq_x * t)
    y = np.sin(freq_y * t)
    ax.plot(x, y)
    ax.set_title(f'{freq_x}:{freq_y}')

plt.tight_layout()
plt.show()

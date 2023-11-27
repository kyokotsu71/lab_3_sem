import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

figure, ax = plt.subplots()

frames = 200
ratio_range = np.linspace(0, 1, frames)


def update(frame):
    ax.clear()
    ratio = ratio_range[frame]
    freq_x = 1
    freq_y = ratio

    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(freq_x * t)
    y = np.sin(freq_y * t)

    ax.plot(x, y)
    ax.set_title(f'{freq_x}:{freq_y}')


animation = FuncAnimation(figure, update, frames, interval=50)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig1, (ax1_1, ax1_2) = plt.subplots(2, 1)
fig1.suptitle('Исходные волны')

fig2, ax2 = plt.subplots()
fig2.suptitle('Результат сложения')

freq1 = 1.0
freq2 = 2.0
amp1 = 1.0
amp2 = 0.5


def update_wave(args):
    freq1 = slider_freq1.val
    freq2 = slider_freq2.val
    amp1 = slider_amp1.val
    amp2 = slider_amp2.val

    t = np.linspace(0, 1, 1000)

    wave1 = amp1 * np.sin(2 * np.pi * freq1 * t)
    wave2 = amp2 * np.sin(2 * np.pi * freq2 * t)

    result = wave1 + wave2

    ax1_1.clear()
    ax1_1.plot(t, wave1)
    ax1_1.set_title('Волна 1')

    ax1_2.clear()
    ax1_2.plot(t, wave2)
    ax1_2.set_title('Волна 2')

    ax2.clear()
    ax2.plot(t, result)
    ax2.set_title('Результат сложения')

    fig1.canvas.draw_idle()
    fig2.canvas.draw_idle()


slider_freq1 = plt.Slider(ax1_1, 'Частота 1', 0.1, 10.0, valinit=freq1)
slider_freq2 = plt.Slider(ax1_2, 'Частота 2', 0.1, 10.0, valinit=freq2)
slider_amp1 = plt.Slider(ax1_1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1)
slider_amp2 = plt.Slider(ax1_2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2)

slider_freq1.on_changed(update_wave)
slider_freq2.on_changed(update_wave)
slider_amp1.on_changed(update_wave)
slider_amp2.on_changed(update_wave)

plt.show()

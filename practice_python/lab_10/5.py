import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z1 = X**2 + Y**2
Z2 = np.log10(Z1)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.set_title('MSE')
ax1.plot_surface(X, Y, Z1, cmap='viridis')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_title('MSE в логарифмическом масштабе')
ax2.plot_surface(X, Y, Z2, cmap='viridis')

plt.show()

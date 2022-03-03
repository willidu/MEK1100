import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 21)
y = x.copy()
vx, vy = np.meshgrid(np.cos(x)*np.sin(y), np.sin(x)*np.cos(y))

plt.quiver(x, y, vx, -vy)
plt.axis('equal')
plt.show()

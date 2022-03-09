import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 6)
x, y = np.meshgrid(t, t)
vx, vy = np.cos(x)*np.sin(y), -np.sin(x)*np.cos(y)

plt.quiver(x, y, vx, vy)
plt.axis('equal')
plt.show()

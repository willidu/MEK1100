import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 1001)
x, y = np.meshgrid(t, t)
z = np.log(np.abs(x)) - y
plt.contour(x, y, z)
plt.show()
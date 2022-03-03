import numpy as np
import matplotlib.pyplot as plt
from velfield import velfield

x, y, u, v = velfield(21)
plt.quiver(x, y, u, v)
plt.axis('equal')
plt.show()

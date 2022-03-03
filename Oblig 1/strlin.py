import numpy as np
import matplotlib.pyplot as plt
from streamfun import streamfun

for n in (5, 30):
    x, y, psi = streamfun(n)
    plt.contour(x, y, psi)
    plt.axis('equal')
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81

for theta in (np.pi/6, np.pi/4, np.pi/3):
    t = np.linspace(0, 2*v0*np.sin(theta)/g, 100)
    x = g*t/(2*v0*np.sin(theta))
    y = x*np.tan(theta)*(1-x)
    plt.plot(x, y)

plt.legend(['pi/6', 'pi/4', 'pi/3'])
plt.xlabel('x*')
plt.ylabel('y*')
plt.show()
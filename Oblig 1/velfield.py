import numpy as np

def velfield(n):
    t = np.linspace(-np.pi/2, np.pi/2, n)
    x, y = np.meshgrid(t, t)
    u, v = np.cos(x)*np.sin(y), np.sin(x)*np.cos(y)
    
    return x, y, u, -v

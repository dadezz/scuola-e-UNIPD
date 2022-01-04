import numpy as np
import matplotlib.pyplot as plt

def parabolaNP (a, b, xmin, xmax, npt):
    x = np.linspace (xmin, xmax, npt)
    y=a*x**2+b
    plt.plot(x,y)
    plt.show()

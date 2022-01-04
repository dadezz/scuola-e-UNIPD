import numpy as np
import matplotlib.pyplot as plt

def gaussiana (a, s, xmin, xmax, n):
    x = np.linspace (xmin, xmax, n)
    y=a*np.exp(-x*x/2*s*s)
    plt.plot(x,y)
    plt.show()

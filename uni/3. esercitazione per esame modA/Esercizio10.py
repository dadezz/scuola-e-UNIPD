#Davide Zambon
import matplotlib.pyplot as plt
import numpy as np

def funzione (A, B, C, N):
    x = np.linspace(-5, 5, N)
    y = A*np.sin(x)+B*np.cos(x**C)
    plt.plot(x, y)
    plt.show()
    return x, y

funzione(6, -1, 3, 1001)
print(funzione(3, 1, 2, 10))

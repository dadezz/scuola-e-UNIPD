#funzione: y=A*x**B*sen(x**C) tra xmin=0 e xmax=4, N punti
#A=2, B=0.5, C=4, N=3001 rappresentati graficamente,
#A=1, B=0,8, C=3, N=7 scritti a video

import numpy as np
import matplotlib.pyplot as plt

def grafica (A, B, C, N):
    x = np.linspace (0, 4, N) #0 è xmin, 4 xmax
    y = A*x**B*np.sin(x**C)
    plt.plot(x,y)
    plt.show()

def stampa (A, B, C, N):
    x = np.linspace (0, 4, N) #0 è xmin, 4 xmax
    #linspace crea una lista tra xmin, xmax di n numeri
    y = A*x**B*np.sin(x**C)
    print (y)

stampa(1, 0.8, 3, 7)
grafica(2, 0.5, 4, 3001)

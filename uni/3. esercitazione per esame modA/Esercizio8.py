#Davide Zambon
import numpy as np
import matplotlib.pyplot as plt

def gauss(N):
    a = np.random.normal(1, 10, N)
    plt.hist(a, 50)
    plt.show()

#gauss(1000)
#gauss(10)

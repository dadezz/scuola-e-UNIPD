import random as rn
import matplotlib.pyplot as plt

def casuale (N, a, b):
    lista = []
    for i in range (N):
        x = rn.randint(a, b)
        lista.append(x)

    plt.hist(lista, 30)
    plt.show()

casuale(7738, -1, 3)

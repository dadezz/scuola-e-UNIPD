#calcoliamo la distribuzione di un dato num di punti casuali tra 0 e 1

import numpy.random as npr
import matplotlib.pyplot as plt

def distribuzione (num_punti, nbin):
    x = npr.random(num_punti)
    plt.hist(x, nbin, normed = True)
    plt.show()

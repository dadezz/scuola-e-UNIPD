import numpy.random as npr
import matplotlib.pyplot as plt

def Gauss (media, sigma, npts, nbin):
    x=npr.normal(media, sigma, npts)
    plt.hist(x, nbin, normed = True)
    plt.show()

Gauss(10, 1, 2000, 100)

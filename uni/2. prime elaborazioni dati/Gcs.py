import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr

dat = np.genfromtxt('Gcs.txt')
mag = dat[:,0]
col = dat[:,1]


plt.plot(mag, col)
plt.show()
def distribuzione (num_punti, nbin):
    x = npr.random(num_punti)
    plt.hist(x, nbin, normed = True)
    plt.show()

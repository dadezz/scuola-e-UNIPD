import numpy as np
import matplotlib.pyplot as plt

#Il file BINARIES.dat contiene delle misure ottenute con Hubble
#relative alla frequenza di binarie in ammassi stellari.
DAT = np.genfromtxt("BINARIES.dat")

x = DAT[:,0] #La massa dell’ammasso (X) alla colonna 1
y = DAT[:,1] #La frazione di binarie (Y) alla colonna 2
err =  DAT[:,2] #L’errore associato alla frazione di binarie (ERR) alla colonna 4

#punto 2: coefficienti della regressione lineare
N = len(x)
sumx = np.sum(x)
sumy = np.sum(y)
sumx2 = np.sum(x*x)
sumxy = np.sum(x*y)
delta = N*sumx2-sumx*sumx
A = (sumx2*sumy-sumx*sumxy)/(delta)
B = (N*sumxy-sumx*sumy)/delta
z = A+B*x

#evidenzio quali sono quelli maggiori a 4.5
xv=x[np.where(x<4.5)]
yv=y[np.where(x<4.5)]
xt=x[np.where(x>=4.5)]
yt=y[np.where(x>=4.5)]
errv=err[np.where(x<4.5)]
errt=err[np.where(x>=4.5)]

#punto 1 e punto 4 insieme: plotting
plt.errorbar(xv, yv, yerr=errv, fmt="or", label="errore")# 'or': o è un punto, g è il colore
plt.errorbar(xt, yt, yerr=errt, fmt="og", label="errore")
plt.plot(xt, yt, "or", label="misure")
plt.plot(xv, yv, "og")

#punto 4
plt.plot(x, z, label="fit")

plt.show()
